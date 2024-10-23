from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils.text import slugify
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Resource, Media, Feature, Comment, Like
from .forms import CommentForm, ResourceForm, MediaForm


def home_page(request):
    """
    Displays the homepage with the most recently published resources

    **Context**

    ``resources``
        A queryset of the latest 4 :model:1post.Resource`
          published objects (status=1), ordered by creation date

    ``images``
        A queryset of :model:`post.Media` related to the 4 resources.

    *Template:*

    :template:`post/index.html`
    """

    queryset = Resource.objects.filter(status=1).order_by("-created_on")
    resources = queryset[:4]
    images = Media.objects.filter(resource__in=resources)

    return render(
        request,
        "post/index.html",
        {"resources": resources, "images": images}
    )


@login_required
def resource_list(request):
    """
    Displays the logged in homepage,
      showing a paginated list of published resources

    **Context**

    ``resources``
        A queryset of the :model:`post.Resource`
          published objects (status=1), ordered by creation date

    ``featured``
        A queryset of the :model:`post.Feature` objects

    ``page_obj``
        A paginated object containing a set of ``resources``
          dependent on the current page number

    *Template:*

    If a page_number is returned from the get function
      the partial template is rendered:

    :template:`post/partials/resource_list.html`

    Otherwise the full template is rendered:

    :template:`post/resource_list.html`
    """
    resources = Resource.objects.filter(status=1).order_by("-created_on")
    features = Feature.objects.all()

    paginator = Paginator(resources, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if page_number:
        return render(request, 'post/partials/resource_list.html',
                      {'page_obj': page_obj})

    return render(
        request,
        "post/resource_list.html",
        {"page_obj": page_obj, "features": features},
    )


@login_required
def user_posts_list(request):
    """
    Displays a list of the logged-in user's posted :model:`post.Resource`
      titles with associated edit and delete buttons.

    **Context**

    ``user_resources``
        A queryset of :model:`post.Resource` objects,
        filtered by logged-in user (author=request.user).

    ``resource_form``
        An instance of :form:`post.ResourceForm`,
          used to edit an existing resource.

    **Template**

    :template:`post/user_posts_list.html`
    """

    if request.user.is_superuser:
        user_resources = Resource.objects.filter(status=1)
    else:
        user_resources = Resource.objects.filter(author=request.user)

    resource_form = ResourceForm()

    return render(
        request,
        "post/user_posts_list.html",
        {
            "user_resources": user_resources,
            "resource_form": resource_form,
        },
    )


@login_required
def resource_detail(request, slug):
    """
    Display an individual :model:`post.Resource`
      with related media and comments.

    **Context**

    ``resource``
        An instance of :model:`post.Resource`, filtered by status and slug

    ``images``
        An queryset of :model:`post.Media` related to the resource

    ``comments``
        An queryset of :model:`post.Comments` related to the resource,
          ordered by creation date

    ``comment_count``
        An integer representing the total number of
        comments related to the resource.

    ``comment_form``
        An instance of :form:`post.CommentForm` for submitting a new comment.

    **POST behavior**

    If a valid POST request is made, a new comment is created,
      linked to the resource, and associated with the logged-in user.

    **Template:**

    :template:`post/resource_detail.html`
    """

    queryset = Resource.objects.filter(status=1)
    resource = get_object_or_404(queryset, slug=slug)
    images = Media.objects.filter(resource=resource.id)
    comments = resource.comments.all().order_by("-created_on")
    comment_count = comments.count()
    like_count = resource.likes.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.resource = resource
            comment.save()

            messages.success(request, "Comment Added")

    comment_form = CommentForm()

    return render(
        request,
        "post/resource_detail.html",
        {
            "resource": resource,
            "images": images,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "like_count": like_count,
        },
    )


@login_required
def resource_preview(request, slug):
    """
    Display an individual :model:`post.Resource` draft.

    **Context**

    ``resources``
        An instance of :model:`post.Resource`,
          filtered by the logged-in user and slug

    ``images``
        An queryset of :model:`post.Media` related to the resource

    **Template**

    :template:`post/resource_preview.html`
    """

    queryset = Resource.objects.filter(author=request.user)
    resource = get_object_or_404(queryset, slug=slug)
    images = Media.objects.filter(resource=resource.id)

    return render(
        request,
        "post/resource_preview.html",
        {
            "resource": resource,
            "images": images,
        },
    )


@login_required
def resource_create(request):
    """
    Handles the creation of a new :model:`post.Resource`
      and its associated media files.

    **Context**

    ``resource_form``
        An instance of :form:`post.ResourceForm`,
        used to create a new resource.

    ``media_form``
        An instance of :form:`post.MediaForm`,
          used to upload media files for the resource.

    **POST behavior**

    - The ``resource_form`` is validated.
    - If valid, the resource is saved with the logged-in user as the author.
    - If `Media` files are added, they are associated with
        the resource and saved.
    - A success message is displayed based on the resource status
        (published or draft), and the user is redirected to
        the appropriate page.

    **Template**

    :template:`post/resource_create.html`
    """

    if request.method == 'POST':
        resource_form = ResourceForm(request.POST)
        media_files = request.FILES.getlist('featured_media')

        if resource_form.is_valid():
            resource = resource_form.save(commit=False)
            resource.slug = slugify(resource.title)
            resource.author = request.user
            resource.save()

            for media_file in media_files:
                Media.objects.create(resource=resource,
                                     featured_media=media_file)

            if resource.status == 1:
                messages.success(request, "Resource Posted")
                return redirect('resource_detail', slug=resource.slug)
            else:
                messages.success(
                    request, "Resource Draft Created" +
                    " (Publish your resource from the 'My Resources' Page)")
                return redirect('resource_preview', slug=resource.slug)

    resource_form = ResourceForm()
    media_form = MediaForm()

    return render(
        request,
        "post/resource_create.html",
        {
            "resource_form": resource_form,
            "media_form": media_form,
        },
    )


@login_required
def resource_edit(request, slug, resource_id):
    """
    Handles the editing of an existing :model:`post.Resource`
      and its associated media files by the logged-in user.

    **Context**

    ``resource``
        An instance of :model:`post.Resource`, retrieved by its ID.

    ``media_files``
        A list of media files (images) uploaded to associate with the resource.

    ``resource_form``
        An instance of :form:`post.ResourceForm`,
          pre-filled with the existing resource data for editing.


    **POST behavior**
    - If valid, the resource is updated with the modified data.
    - If new media files are added, they are saved and
        associated with the resource.
    - A success message is displayed when the resource is successfully updated,
        and the user is redirected to the "My Resources" page.
    - If the form is invalid or the user is not the author,
        an error message is displayed.

    **Template**

    :template:`post/user_posts_list.html`
    """

    if request.method == "POST":

        resource = get_object_or_404(Resource, pk=resource_id)
        media_files = request.FILES.getlist('featured_media')

        if resource.author == request.user:
            resource_form = ResourceForm(data=request.POST, instance=resource)

        if resource_form.is_valid() and resource.author == request.user:
            resource = resource_form.save(commit=False)
            resource.slug = slugify(resource.title)
            resource.save()

            for media_file in media_files:
                Media.objects.create(resource=resource,
                                     featured_media=media_file)

            if resource.status == 1:
                messages.success(request, "Resource Posted")
                return redirect('resource_detail', slug=resource.slug)
            else:
                messages.success(
                    request, "Resource Draft Created" +
                    " (Publish your resource from the 'My Resources' Page)")
                return redirect('resource_preview', slug=resource.slug)

        else:
            messages.error(request, "Error updating")


@login_required
def resource_delete(request, slug):
    """
    Handles the deletion of an existing :model:`post.Resource`
      by the logged-in user.

    **Context**

    ``resource``
        An instance of :model:`post.Resource`,
          filtered by the slug and logged-in user.

    **POST behavior**

    - The resource is retrieved based on the slug and the logged-in user.
    - If the logged-in user is the author of the resource,
        it is deleted, and a success message is displayed.
    - If an error occurs, an error message is displayed.

    **Template**

    :template:`post/user_posts_list.html`
    """

    queryset = Resource.objects.filter(author=request.user)
    resource = get_object_or_404(queryset, slug=slug)

    if resource.author == request.user:
        resource.delete()
        messages.success(request, 'Resource deleted!')
    else:
        messages.error(request, 'An error occurred.')

    return redirect('user_posts_list')


@login_required
def comment_edit(request, slug, comment_id):
    """
    Handles the editing of an existing :model:`post.Comment`
      for a published :model:`post.Resource`.

    **Context**

    ``resource``
        An instance of :model:`post.Resource`, filtered by status and slug.

    ``comment``
        An instance of :model:`post.Comment`, retrieved by its ID.

    ``comment_form``
        An instance of :form:`post.CommentForm`, pre-filled with
        the existing comment data for editing.

    **POST behavior**

    - The ``comment_form`` is validated.
    - If valid and the logged-in user is the comment author,
        the comment is updated and saved.
    - If successful, a success message is displayed.
    - If the form is invalid or the user is not the author,
        an error message is shown.

    **Template**

    :template:`post/resource_detail.html`
    """

    if request.method == "POST":

        queryset = Resource.objects.filter(status=1)
        resource = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.resource = resource
            comment.save()
            messages.success(request, "Comment updated")
        else:
            messages.error(request, "Error updating")

    return HttpResponseRedirect(reverse('resource_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    Handles the deletion of an existing :model:`post.Comment`
      for a published :model:`post.Resource`.

    **Context**

    ``resource``
        An instance of :model:`post.Resource`, filtered by slug and status.

    ``comment``
        An instance of :model:`post.Comment`, retrieved by its ID.

    **POST behavior**

    - The comment is retrieved by its ID.
    - If the logged-in user is the author of the comment,
        the comment is deleted and a success message is displayed.
    - If the user is not the author, an error message is shown,
        and the comment is not deleted.

    **Template**
    :template:`post/resource_detail.html`
    """

    queryset = Resource.objects.filter(status=1)
    resource = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('resource_detail', args=[slug]))


@login_required
def like_resource(request, slug):
    """
    Handles the liking or un-liking of an existing :model:`post.Resource`
    by the logged-in user.

    **Context**

    ``resource``
        An instance of :model:`post.Resource`, filtered by status and slug.

    **POST behavior**

    - The ``resource`` is retrieved based on the slug.
    - If a like from the logged-in user already exists for the ``resource``,
        the like is removed, and a success message is displayed.
    - If no like exists, a new like is created for the ``resource``,
        and a success message is displayed.

    **Template**

    :template:`post/resource_detail.html`
    """
    if request.method == 'POST' and request.user.is_authenticated:
        queryset = Resource.objects.filter(status=1)
        resource = get_object_or_404(queryset, slug=slug)

        liked_resource = Like.objects.filter(resource=resource, author=request.user).exists()

        if liked_resource:
            Like.objects.filter(resource=resource, author=request.user).delete()
            messages.success(request, 'Un-Liked Resource')
        else:
            Like.objects.create(resource=resource, author=request.user)
            messages.success(request, 'Liked Resource!')

        return HttpResponseRedirect(reverse('resource_detail', args=[slug]))
    else:
        messages.error(request, 'An error occurred!')
        return HttpResponseRedirect(reverse('resource_detail', args=[slug]))
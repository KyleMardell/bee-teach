from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from .forms import CommentForm, ResourceForm
from .models import Resource, Comment, Like


class TestPostViews(TestCase):

    def setUp(self):

        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword"
        )

        self.client.login(
            username="myUsername",
            password="myPassword"
        )

        self.resource = Resource.objects.create(
                        title="Resource Title",
                        author=self.user,
                        slug="resource-title",
                        key_stage="0",
                        content="Resource content",
                        links="www.testlinks.com",
                        status=1)

        self.draft_resource = Resource.objects.create(
                        title="Draft Resource Title",
                        author=self.user,
                        slug="draft-resource-title",
                        key_stage="0",
                        content="Draft resource content",
                        links="www.testlinks.com",
                        status=0)

        # Create additional resources to test the home page view.
        for i in range(4):
            Resource.objects.create(
                title=f"Resource Title {i}",
                author=self.user,
                slug=f"resource-title-{i}",
                key_stage='1',
                content=f"Resource content {i}",
                links="www.testlinks.com",
                status=1
            )

        self.comment = Comment.objects.create(
            body="Test Comment",
            resource=self.resource,
            author=self.user
        )

    # Index Page

    def test_index_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_index_page_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'post/index.html')

    def test_index_page_shows_four_latest_resources(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['resources']), 4)
        self.assertContains(response, "Resource Title 0")
        self.assertContains(response, "Resource Title 3")

    def test_index_page_shows_only_published_resources(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Draft Resource Title")

    # Home Page (resource_list)

    def test_home_page_status_code(self):
        response = self.client.get(reverse('resource_list'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_requires_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('resource_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/resource_list/')

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('resource_list'))
        self.assertTemplateUsed(response, 'post/resource_list.html')

    def test_partial_template(self):
        response = self.client.get(reverse('resource_list') + '?page=1')
        self.assertTemplateUsed(response, 'post/partials/resource_list.html')

    def test_home_page_shows_only_published_resources(self):
        response = self.client.get(reverse('resource_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Draft Resource Title")

    def test_featured_resources(self):
        response = self.client.get(reverse('resource_list'))
        self.assertIn('features', response.context)

    # User Posts List Page

    def test_user_resources_page_status(self):
        response = self.client.get(reverse('user_posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_user_resources_page_requires_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('user_posts_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/user_posts_list/')

    def test_user_resources_page_uses_correct_template(self):
        response = self.client.get(reverse('user_posts_list'))
        self.assertTemplateUsed(response, 'post/user_posts_list.html')

    def test_user_resources_shows_published_resources(self):
        response = self.client.get(reverse('user_posts_list'))
        self.assertContains(response, 'Resource Title')

    def test_user_resources_shows_draft_resources(self):
        response = self.client.get(reverse('user_posts_list'))
        self.assertContains(response, 'Draft Resource Title')

    # Resource Detail Page

    def test_resource_detail_page_status_code(self):
        response = self.client.get(reverse(
            'resource_detail', args=['resource-title']))
        self.assertEqual(response.status_code, 200)

    def test_resource_detail_page_requires_authentication(self):
        self.client.logout()
        response = self.client.get(reverse(
            'resource_detail', args=['resource-title']))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/resource-title/resource_detail')

    def test_resource_detail_uses_correct_template(self):
        response = self.client.get(reverse(
            'resource_detail', args=['resource-title']))
        self.assertTemplateUsed(response, 'post/resource_detail.html')

    def test_resource_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'resource_detail', args=['resource-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Resource Title", response.content)
        self.assertIn(b"Resource content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        post_data = {'body': 'This is a test comment.'}
        response = self.client.post(reverse(
            'resource_detail', args=['resource-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment Added', response.content)
        self.assertIn(b'This is a test comment.', response.content)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Comment Added')

    # Resource Preview

    def test_resource_preview_page_status_code(self):
        response = self.client.get(reverse(
            'resource_preview', args=['resource-title']))
        self.assertEqual(response.status_code, 200)

    def test_resource_preview_page_requires_authentication(self):
        self.client.logout()
        response = self.client.get(reverse(
            'resource_preview', args=['resource-title']))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/resource-title/resource_preview')

    def test_resource_preview_uses_correct_template(self):
        response = self.client.get(reverse(
            'resource_preview', args=['resource-title']))
        self.assertTemplateUsed(response, 'post/resource_preview.html')

    # Resource Create

    def test_resource_create_page_status_code(self):
        response = self.client.get(reverse('resource_create'))
        self.assertEqual(response.status_code, 200)

    def test_resource_create_page_requires_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('resource_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/resource_create/')

    def test_resource_create_page_uses_correct_template(self):
        response = self.client.get(reverse('resource_create'))
        self.assertTemplateUsed(response, 'post/resource_create.html')

    def test_resource_create_page_with_resource_form(self):
        response = self.client.get(reverse('resource_create'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context['resource_form'], ResourceForm)

    def test_successful_published_resource_form_submission(self):
        post_data = {
            'title': "Published New Resource Title",
            'key_stage': "0",
            'content': "Published resource content",
            'links': "www.testlinks.com",
            'status': "1"
        }
        response = self.client.post(reverse('resource_create'), post_data)
        self.assertEqual(response.status_code, 302)
        published_resource = Resource.objects.get(
            title="Published New Resource Title")
        self.assertRedirects(response, reverse(
            'resource_detail', kwargs={'slug': published_resource.slug}))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Resource Posted')

    def test_successful_draft_resource_form_submission(self):
        post_data = {
            'title': "Draft New Resource Title",
            'key_stage': "0",
            'content': "Draft resource content",
            'links': "www.testlinks.com",
            'status': "0"
        }
        response = self.client.post(reverse('resource_create'), post_data)
        self.assertEqual(response.status_code, 302)
        draft_resource = Resource.objects.get(title="Draft New Resource Title")
        self.assertRedirects(
            response, reverse(
                'resource_preview', kwargs={'slug': draft_resource.slug}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(
            messages[0]), "Resource Draft Created (Publish your " +
            "resource from the 'My Resources' Page)")

    # Resource Edit

    def test_successful_published_resource_edit_submission(self):
        post_data = {
            'title': "Updated Resource Title",
            'key_stage': "1",
            'content': "Updated resource content",
            'links': "www.updatedlinks.com",
            'status': "1",
        }
        response = self.client.post(
            reverse('resource_edit', args=[
                'resource-title', self.resource.id]), post_data)
        self.assertEqual(response.status_code, 302)
        updated_resource = Resource.objects.get(id=self.resource.id)
        self.assertEqual(updated_resource.title, "Updated Resource Title")
        self.assertRedirects(
            response, reverse('resource_detail', kwargs={
                'slug': updated_resource.slug}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Resource Posted')

    def test_successful_draft_resource_edit_submission(self):
        post_data = {
            'title': "Updated Resource Title",
            'key_stage': "1",
            'content': "Updated resource content",
            'links': "www.updatedlinks.com",
            'status': "0",
        }
        response = self.client.post(
            reverse('resource_edit', args=[
                'resource-title', self.resource.id]), post_data)
        self.assertEqual(response.status_code, 302)
        updated_resource = Resource.objects.get(id=self.resource.id)
        self.assertEqual(updated_resource.title, "Updated Resource Title")
        self.assertRedirects(
            response, reverse(
                'resource_preview', args=[updated_resource.slug]))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(
            messages[0]), "Resource Draft Created (Publish your " +
            "resource from the 'My Resources' Page)")

    # Resource Delete

    def test_resource_delete_success(self):
        resource_count = Resource.objects.count()
        response = self.client.post(
            reverse('resource_delete', args=[self.resource.slug]))
        after_delete_resource_count = Resource.objects.count()
        self.assertEqual(after_delete_resource_count, resource_count - 1)
        self.assertRedirects(response, reverse('user_posts_list'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Resource deleted!')

    def test_resource_delete_not_author(self):
        self.client.logout()
        test_user = User.objects.create_user(
            username="TestUser",
            password="TestUsersPassword",
        )
        self.client.login(username='TestUser', password='TestUsersPassword')
        resource_count = Resource.objects.count()
        response = self.client.post(
            reverse('resource_delete', args=[self.resource.slug]))
        after_delete_resource_count = Resource.objects.count()
        self.assertEqual(after_delete_resource_count, resource_count)
        self.assertEqual(response.status_code, 404)

    # Comment Edit

    def test_successful_comment_edit(self):
        post_data = {'body': 'This is an edited test comment.'}
        response = self.client.post(reverse(
            'comment_edit', args=[
                'resource-title', self.comment.id]), post_data)
        self.assertEqual(response.status_code, 302)
        updated_comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(
            updated_comment.body, "This is an edited test comment.")
        self.assertRedirects(response, reverse(
            'resource_detail', args=[self.resource.slug]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Comment updated')

    def test_comment_edit_not_author(self):
        self.client.logout()
        test_user = User.objects.create_user(
            username="TestUser",
            password="TestUsersPassword",
        )
        self.client.login(username='TestUser', password='TestUsersPassword')
        post_data = {'body': 'This is an edited test comment.'}
        response = self.client.post(reverse(
            'comment_edit', args=[
                'resource-title', self.comment.id]), post_data)
        self.assertEqual(response.status_code, 302)
        updated_comment = Comment.objects.get(id=self.comment.id)
        self.assertNotEqual(
            updated_comment.body, "This is an edited test comment.")
        self.assertRedirects(response, reverse(
            'resource_detail', args=[self.resource.slug]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Error updating')

    # Comment Delete

    def test_comment_delete_success(self):
        comment_count = Comment.objects.count()
        response = self.client.post(
            reverse('comment_delete', args=[
                self.resource.slug, self.comment.id]))
        after_delete_comment_count = Comment.objects.count()
        self.assertEqual(after_delete_comment_count, comment_count - 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'resource_detail', args=[self.resource.slug]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Comment deleted!')

    def test_comment_delete_not_author(self):
        self.client.logout()
        test_user = User.objects.create_user(
            username="TestUser",
            password="TestUsersPassword",
        )
        self.client.login(username='TestUser', password='TestUsersPassword')
        comment_count = Comment.objects.count()
        response = self.client.post(
            reverse('comment_delete', args=[
                self.resource.slug, self.comment.id]))
        after_delete_comment_count = Comment.objects.count()
        self.assertEqual(after_delete_comment_count, comment_count)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'resource_detail', args=[self.resource.slug]))

    # Resource Likes

    def test_successful_resource_like(self):
        like_count = Like.objects.count()
        response = self.client.post(
            reverse('like_resource', args=[self.resource.slug]))
        after_like_count = Like.objects.count()
        self.assertEqual(after_like_count, like_count + 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'resource_detail', args=[self.resource.slug]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Liked Resource!')

    def test_successful_resource_unlike(self):
        self.new_like = Like.objects.create(
                        resource=self.resource,
                        author=self.user
        )
        like_count = Like.objects.count()
        response = self.client.post(
            reverse('like_resource', args=[self.resource.slug]))
        after_like_count = Like.objects.count()
        self.assertEqual(after_like_count, like_count - 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'resource_detail', args=[self.resource.slug]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Un-Liked Resource')

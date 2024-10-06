from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

KEYSTAGE = ((0, "Early Years"), (1, "Key Stage 1"),
            (2, "Key Stage 2"), (3, "Key Stage 3"))
STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Resource(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="resource_posts"
    )
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    key_stage = models.IntegerField(choices=KEYSTAGE, default=0)
    content = models.TextField(blank=True)
    links = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Sorts newest first, remove '-' to sort oldest first
    class Meta:
        ordering = ["-created_on"]

    # Represents self instance in admin panel
    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Like(models.Model):
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, related_name="likes"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liker"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    # Ensures that a user can only like a resource once
    class Meta:
        unique_together = ('resource', 'author')

    def __str__(self):
        return f'Like by {self.author} on {self.resource}'


class Media(models.Model):
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, related_name="media"
    )
    # This field can store either images or PDFs
    featured_media = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Media for {self.resource}'


class Feature(models.Model):
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE,
        related_name="features", blank=True, null=True
    )
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # Sorts newest first, remove '-' to sort oldest first
    class Meta:
        ordering = ["-created_on"]

    # Represents self instance in admin panel
    def __str__(self):
        return f"{self.title}"

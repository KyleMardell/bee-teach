from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Resource, Media

class TestPostViews(TestCase):

    def setUp(self):

        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
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

        for i in range(4):  # Create additional resources to test the home page view.
            Resource.objects.create(
                title=f"Resource Title {i}",
                author=self.user,
                slug=f"resource-title-{i}",
                key_stage='1',
                content=f"Resource content {i}",
                links="www.testlinks.com",
                status=1
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

    # Resource Detail Page

    def test_resource_detail_page_status_code(self):
        response = self.client.get(reverse(
            'resource_detail', args=['resource-title']))
        self.assertEqual(response.status_code, 200)

    def test_resource_detail_uses_correct_template(self):
        response = self.client.get(reverse(
            'resource_detail', args=['resource-title']))
        self.assertTemplateUsed(response, 'post/resource_detail.html')

    def test_render_resource_detail_page_with_comment_form(self):
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

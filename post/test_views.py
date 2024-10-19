from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm, ResourceForm
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

    # Resource Edit

    def test_successful_published_resource_edit_submission(self):
        post_data = {
            'title': "Updated Resource Title",
            'key_stage': "1",
            'content': "Updated resource content",
            'links': "www.updatedlinks.com",
            'status': "1",
        }
        response = self.client.post(reverse('resource_edit', args=['resource-title', self.resource.id]), post_data)
        self.assertEqual(response.status_code, 302)
        updated_resource = Resource.objects.get(id=self.resource.id)
        self.assertEqual(updated_resource.title, "Updated Resource Title")
        self.assertRedirects(response, reverse('resource_detail', kwargs={'slug': updated_resource.slug}))

    def test_successful_draft_resource_edit_submission(self):
        post_data = {
            'title': "Updated Resource Title",
            'key_stage': "1",
            'content': "Updated resource content",
            'links': "www.updatedlinks.com",
            'status': "0",
        }
        response = self.client.post(reverse('resource_edit', args=['resource-title', self.resource.id]), post_data)
        self.assertEqual(response.status_code, 302)
        updated_resource = Resource.objects.get(id=self.resource.id)
        self.assertEqual(updated_resource.title, "Updated Resource Title")
        self.assertRedirects(response, reverse('resource_preview', kwargs={'slug': updated_resource.slug}))
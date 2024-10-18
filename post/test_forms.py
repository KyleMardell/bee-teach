from django.test import TestCase
from .forms import CommentForm, ResourceForm


class TestCommentForm(TestCase):  # Comment Form Tests

    # Assert True

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a valid test comment'})
        self.assertTrue(comment_form.is_valid(),
                        msg='Comment form is not valid')

    # Assert False

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg='Comment form is valid')


class TestResourceForm(TestCase):  # Resource Form Tests

    # Assert True

    def test_form_is_valid_with_empty_content_and_links_draft(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',  # key_stage 0: early years
            'content': '',
            'links': '',
            'status': '0'  # status 0: draft
        })
        self.assertTrue(resource_form.is_valid(),
                        msg='Resource form is not valid')

    def test_form_is_valid_with_empty_content_and_links_published(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',
            'content': '',
            'links': '',
            'status': '1'  # status 1: published
        })
        self.assertTrue(resource_form.is_valid(),
                        msg='Resource form is not valid')

    def test_form_is_valid_full_input(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',
            'content': 'Test Content',
            'links': 'www.testlink.com',
            'status': '0'
        })
        self.assertTrue(resource_form.is_valid(),
                        msg='Resource form is not valid')

    def test_form_is_valid_with_empty_links(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',
            'content': 'Test Content',
            'links': '',
            'status': '0'
        })
        self.assertTrue(resource_form.is_valid(),
                        msg='Resource form is not valid')

    def test_form_is_valid_with_empty_content(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',
            'content': '',
            'links': 'www.testlink.com',
            'status': '0'
        })
        self.assertTrue(resource_form.is_valid(),
                        msg='Resource form is not valid')

    def test_form_is_valid_title_character_limit(self):  # 100 character limit
        resource_form = ResourceForm({
            'title': 'CharactersCharactersCharactersCharacters' +
            'CharactersCharactersCharactersCharactersCharactersCharacters',
            'key_stage': '0',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertTrue(resource_form.is_valid(),
                        msg='Resource form is not valid')

    def test_form_is_valid_key_stage_one(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '1',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertTrue(resource_form.is_valid(),
                        msg='Resource form is not valid')

    def test_form_is_valid_key_stage_two(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '2',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertTrue(resource_form.is_valid(),
                        msg='Resource form is not valid')

    def test_form_is_valid_key_stage_three(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '3',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertTrue(resource_form.is_valid(),
                        msg='Resource form is not valid')

    # Assert False

    def test_form_is_invalid_blank_form(self):
        resource_form = ResourceForm({
            'title': '',
            'key_stage': '0',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_missing_key_stage(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_missing_status(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',
            'content': '',
            'links': '',
            'status': ''
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_negative_one_key_stage(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '-1',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_negative_zero_key_stage(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '-0',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_negative_one_status(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',
            'content': '',
            'links': '',
            'status': '-1'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_negative_zero_status(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',
            'content': '',
            'links': '',
            'status': '-0'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_top_edge_key_stage(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '4',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_top_edge_status(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',
            'content': '',
            'links': '',
            'status': '2'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_non_numeric_key_stage(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': 'A',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_non_numeric_status(self):
        resource_form = ResourceForm({
            'title': 'Test Resource',
            'key_stage': '0',
            'content': '',
            'links': '',
            'status': 'A'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_overly_long_title(self):  # 100 character limit
        resource_form = ResourceForm({
            'title': 'CharactersCharactersCharactersCharactersCharacters' +
            'CharactersCharactersCharactersCharactersCharacters1',
            'key_stage': '0',
            'content': '',
            'links': '',
            'status': '0'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')

    def test_form_is_invalid_only_optional_fields(self):
        resource_form = ResourceForm({
            'title': '',
            'key_stage': '0',
            'content': 'Test Content',
            'links': 'www.testlink.com',
            'status': '0'
        })
        self.assertFalse(resource_form.is_valid(),
                         msg='Resource form is valid')
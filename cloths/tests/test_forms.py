from django.test import TestCase

from cloths.forms import CommentForm

class TestCommentForm(TestCase):
    def test_comment_form_valid_data(self):
        comment_form = CommentForm(data={
            'body' : 'test valid comment form',
        })
        self.assertTrue(comment_form.is_valid())
    
    def test_comment_form_invalid_data(self):
        comment_form = CommentForm(data={})
        self.assertFalse(comment_form.is_valid())
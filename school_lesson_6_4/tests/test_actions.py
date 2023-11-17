from .common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import UserError


@tagged('post_install', '-at_install', 'library', 'action', 'odooschool')
class TestAccessRights(TestCommon):

    def test_action_take_in(self):
        self.book_demo.write({'reader_id': self.library_user.partner_id.id})

        # A library user can't return a book himself
        with self.assertRaises(UserError):
            self.book_demo.with_user(self.library_user).action_take_in()

        # A library admin can return a book
        self.book_demo.with_user(self.library_admin).action_take_in()
        self.assertFalse(self.book_demo.reader_id)

    # Task 6-4.3
    def test_action_scrap_book(self):
        self.book_demo.with_user(self.library_user).action_scrap_book()
        self.assertFalse(self.book_demo.active)

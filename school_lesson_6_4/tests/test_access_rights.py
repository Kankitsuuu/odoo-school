from .common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install', 'library', 'access', 'odooschool')
class TestAccessRights(TestCommon):

    def test_01_library_user_access_rights(self):
        with self.assertRaises(AccessError):
            self.env['library.book'].with_user(self.library_user).create(
                {'name': 'Test Book'})
        with self.assertRaises(AccessError):
            self.book_demo.with_user(self.library_user).unlink()

        # Task 6-4.2
        with self.assertRaises(AccessError):
            self.env['library.author'].with_user(self.library_user).create({
                'first_name': 'Alexandre',
                'last_name': 'Dumas',
            })

    def test_02_library_admin_access_rights(self):
        book = self.env['library.book'].with_user(self.library_admin).create(
            {'name': 'Test Book'})
        book.with_user(self.library_admin).read()
        book.with_user(self.library_admin).write({'name': 'Test Book II'})
        book.with_user(self.library_admin).unlink()

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Book, CustomUser, UserProfile
from bookshelf.group_permissions import create_group_permission


# Create your tests here.
class GroupPermissionTest(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_user(
            username='testuseradmin',
            password='TestPassword@1',
            email='testuseradmin@mail.com',
            date_of_birth='2002-12-01'
        )

        self.admin_user.userprofile.role = 'Admin'
        self.admin_user.userprofile.save()


        group = create_group_permission('Admins')
        self.admin_user.groups.add(group)

        self.editor_user = get_user_model().objects.create_user(
            username='testusereditor',
            password='TestPassword@2',
            email='testusereditor@mail.com',
            date_of_birth='2002-12-01'
        )

        self.editor_user.userprofile.role = 'Librarian'
        self.editor_user.userprofile.save()
        
        group = create_group_permission('Editors')
        self.editor_user.groups.add(group)

        self.viewer_user = get_user_model().objects.create_user(
            username='testuserviewer',
            password='TestPassword@1',
            email='testusermember@mail.com',
            date_of_birth='2002-12-01'
        )

        group = create_group_permission('Viewers')
        self.viewer_user.groups.add(group)

    # test for admin user
    def test_admin_group_permission(self):
        # simulate login user
        self.client.force_login(self.admin_user)
        response = self.client.get(reverse('admin_view'))

        self.assertTrue(self.admin_user.groups.filter(name='Admins').exists())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is the admin dashboard.')

    # test for editor user
    def test_editor_group_permission(self):
        # simulate login user
        self.client.force_login(self.editor_user)
        response = self.client.get(reverse('librarian_view'))
        
        self.assertTrue(self.editor_user.groups.filter(name='Editors').exists())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is the librarian dashboard.')

    # test for viewer user
    def test_viewer_group_permission(self):
        # simulate login user
        self.client.force_login(self.viewer_user)
        response = self.client.get(reverse('member_view'))

        self.assertTrue(self.viewer_user.groups.filter(name='Viewers').exists())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is the member dashboard.')


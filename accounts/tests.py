from django.test import TestCase
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email='user@gmail.com', password="test123")
        User.objects.create_superuser(email='superuser@gmail.com', password='123467')
        User.objects.create_staffuser(email='staffuser@gmail.com', password='1234567')

    
    def test_normal_user(self):
        user = User.objects.get(email='user@gmail.com')
        self.assertIs(user.is_admin, False, "A standard user can not be admin")
        self.assertIs(user.is_staff, False, "A standard user can not be staff member")
        self.assertIs(user.is_active, True, "User should be activated by default")
        

    def test_superuser(self):
        superuser = User.objects.get(email='superuser@gmail.com')
        self.assertIs(superuser.is_admin, True, "A Super user must be admin")
        self.assertIs(superuser.is_staff, True, "A Super user must be staff also")
        self.assertIs(superuser.is_active, True, "User should be activated by default")
    
    def test_staffuser(self):
        staffuser = User.objects.get(email='staffuser@gmail.com')
        self.assertIs(staffuser.is_admin, False, "A staff user can not be admin")
        self.assertIs(staffuser.is_staff, True, "A staff user must be have staff flag")
        self.assertIs(staffuser.is_active, True, "User should be activated by default")
    
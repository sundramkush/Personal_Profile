from django.test import TestCase
from profile_register.models import profile
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
from django.db import IntegrityError
from django.urls import reverse, resolve, NoReverseMatch
from profile_register.views import * 
from django.test.client import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user('user1')
        user2 = User.objects.create_user('user2')
        user3 = User.objects.create_user('user3')
        profile.objects.create(name="xxxxxx", past_address="aaaaaa", current_address='bbbbbbb', ph_number='12345', user_id= user1)
        profile.objects.create(name="yyyyyy", current_address="bbbbb", ph_number='12345', user_id= user2)
        profile.objects.create(name="yyyyyy", current_address="bbbbb", ph_number='12345', user_id= user3)

    def test_database(self):
        user = User.objects.create_user('user')
        with self.assertRaises(TypeError):
            profile.objects.create(name="yyyyyy", current_address="bbbbb", ph_number='12345', user_id= user, path = 'hello')
    
    def test_profile_object(self):
        """Testing object creation"""
        o1 = profile.objects.get(name="xxxxxx")
        self.assertEqual(o1.past_address, 'aaaaaa')
    
    def test_profile_object_creation_error_with_existing_user(self):
        """Testing object creation error"""
        user = User.objects.get(username = 'user2') 
        with self.assertRaises(IntegrityError):
            profile.objects.create(name="yyyyyy", past_address="aaaaaa", current_address="bbbbb", ph_number='12345', user_id= user)
    
    def test_user_creation_error_with_existing_username(self):
        """Testing user creation error""" 
        with self.assertRaises(IntegrityError):
            User.objects.create_user('user2')
    
    
    def test_profiles_equality_and_nonequality(self):
        """Testing object equality)"""
        o1 = profile.objects.get(user_id = User.objects.get(username = 'user1'))
        o2 = profile.objects.get(user_id = User.objects.get(username = 'user2'))
        o3 = profile.objects.get(user_id = User.objects.get(username = 'user3'))
        self.assertNotEqual(o1,o2)
        self.assertNotEqual(o2,o3)
        self.assertEqual(o2.name, o3.name)
        self.assertEqual(o2.current_address, o3.current_address)
        self.assertEqual(o2.ph_number, o3.ph_number)
        self.assertNotEqual(o2.user_id, o3.user_id)
    
    def test_profiles_multiple_object_return_error(self):
        """Testing object get method (model)"""
        with self.assertRaises(MultipleObjectsReturned):
            profile.objects.get(name = 'yyyyyy')
    
    def test_home_url(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(resolve(url).func, home)

    def test_login_url(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(resolve(url).func, login)
    
    def test_logout_url(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(resolve(url).route, 'logout')
    
    def test_list_url(self):
        url = reverse('profile_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(resolve(url).func, list)
    
    def test_insert_url(self):
        url = reverse('profile_insert')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(resolve(url).func, form)
    
    def test_update_url(self):
        with self.assertRaises(NoReverseMatch):
            url = reverse('profile_update')
        obj = profile.objects.get(name = 'xxxxxx').pk
        url = reverse('profile_update',args = [obj])
        try:
            response = self.client.get(url)
        except profile.DoesNotExist:
            self.assertEqual(response.status_code, 200)
        self.assertEquals(resolve(url).func, form)

    def test_delete_url(self):
        with self.assertRaises(NoReverseMatch):
            url = reverse('profile_delete')
        obj = profile.objects.get(name = 'xxxxxx').pk
        url = reverse('profile_delete', args= [obj])
        #print(profile.objects.all())
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(resolve(url).func, delete)

    def test_object_insertion(self):
        user = User.objects.create_user('user')
        profile.objects.create(name="abcd", past_address="aaaaaa", current_address='bbbbbbb', ph_number='12345', user_id= user)
        self.assertEquals(profile.objects.filter(name = 'abcd').exists(), True)
        self.assertEquals(profile.objects.get(name = 'abcd').user_id, user)
    
    def test_object_deletion(self):
        del_obj = profile.objects.get(name = "xxxxxx")
        del_obj.delete()
        with self.assertRaises(profile.DoesNotExist):
            profile.objects.get(name = "xxxxxx")
    
    def test_object_update(self):
        obj = profile.objects.get(name = 'xxxxxx')
        id_obj = obj.pk
        url = reverse('profile_update', args=[id_obj])
        response = self.client.get(url)
        self.assertContains(response, "xxxxxx")
        profile_data = profilesform(instance=obj).initial
        profile_data['name'] = "aaaaaa"
        response = self.client.post(reverse('profile_update', args=[id_obj]), profile_data)
        obj.refresh_from_db()
        with self.assertRaises(profile.DoesNotExist):
            profile.objects.get(name = "xxxxxx")
        self.assertEquals(profile.objects.get(name = "aaaaaa").pk, id_obj)





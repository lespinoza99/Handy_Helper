from django.db import models
import re
# Create your models here.


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['fname'] = "First Name must be at least 2 character"

        if len(postData['last_name']) < 2:
            errors['lname'] = 'Last Name must be at least 2 character'

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'

        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'

        if postData['password'] != postData['confirm_password']:
            errors['invalid_password'] = "Password and confirm password doesn't match!"

        return errors

    def login_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        return errors

    def job_validator(self, postData):
        errors = {}

        if len(postData['title']) < 1:
            errors['title'] = 'Title must be at least 1 character!'
        
        if len(postData['location']) < 3:
            errors['location'] = 'Location must be at least 3 characters!'
        
        if len(postData['desc']) < 1:
            errors['description'] = 'Description must be at least 3 characters!'
        
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    test_edit = models.CharField(max_length = 255, default = 'Edit_test')
    objects = UserManager()


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edit = models.CharField(max_length = 255, default = 'Edit')
    user = models.ForeignKey(User, related_name='jobs', on_delete = models.CASCADE)
    objects = UserManager()


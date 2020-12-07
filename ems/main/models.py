from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save()
        return user_obj

    def create_staff(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_admin=True)
        return user


class CustomUser(AbstractBaseUser):
    blood = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    sex = (
        ('male', 'male'),
        ('female', 'female'),
    )
    id = models.AutoField(primary_key=True)
    is_employee = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    full_name = models.CharField(max_length=200, null=False)
    department = models.CharField(max_length=100, null=False)
    designation = models.CharField(max_length=100, null=False)
    adn_id = models.IntegerField(null=True)
    password = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    alternate_email = models.EmailField(max_length=100, default='null', null=False)
    phone = models.CharField(max_length=100, null=False)
    alternate_phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=sex, default='null', null=False)
    dob = models.DateField(null=True)
    join = models.DateField(null=True)
    address = models.CharField(max_length=200, null=False)
    blood_group = models.CharField(max_length=20, choices=blood, default='null', null=False)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

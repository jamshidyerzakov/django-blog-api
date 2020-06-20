from django.db import models
from django.contrib.auth.models import (
    AbstractUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self,
                    email,
                    first_name=None,
                    last_name=None,
                    password=None,
                    img=None,
                    is_active=True,
                    is_staff=False,
                    is_admin=False,
                    is_superuser=False,
                    ):
        if not email:
            raise ValueError("Users must have an email address")
        # if not password:
        #     raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            img=img,
        )
        user_obj.is_active = is_active
        user_obj.is_admin = is_admin
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser

        user_obj.set_password(password)
        user_obj.save(using=self.db)
        return user_obj

    def create_staffuser(self, email, password=None, first_name=None, last_name=None, img=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            img=img,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name=None, password=None, first_name=None, last_name=None, img=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            img=img,
            is_staff=True,
            is_admin=True,
            is_superuser=True,
        )
        return user


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name="email")
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    img = models.ImageField(verbose_name="Image")
    date_joined = models.DateTimeField(auto_now_add=True)
    liked_posts = models.ManyToManyField('post.Post', related_name='liked_posts', verbose_name='Liked Post', blank=True)
    is_superuser = None
    groups = None
    # user_permissions = None
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # email and password are required
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        return self.email

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    # @property
    # def is_staff(self):
    #     return self.is_staff
    #
    # @property
    # def is_admin(self):
    #     return self.is_admin
    #
    # @property
    # def is_active(self):
    #     return self.is_active
    #
    # @property
    # def is_superuser(self):
    #     return self.superuser

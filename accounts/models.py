"""
There are 2 main types of users derived from User model in this project:
— Authors :
     — They are admins of the blog
     — Only Authors can add posts to the blog
     — By default: is_superuser and is_staff is True

— Readers :
     — Do not have any privileges
     — They can follow authors' posts or categories of posts
     — They have liked_posts field to save their favourite posts

Email is used to register and log-in (No username)
"""
from django.contrib import auth
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
     Custom user manager to create and save a user with the given email and password.
    """
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Creating author if is_author is true else creating reader.

        Overriding this method, because many 3rd-party packages use
        this method to create users.

        In this project we use only Author or Reader objects as users.
        They are related to User as one to one field.

        """
        if extra_fields.get('is_author', None):
            return Author.objects.create_author(email, password, **extra_fields)
        else:
            return Reader.objects.create_reader(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class AuthorManager(BaseUserManager):
    """
     Custom author manager to create and save an author with the given email, password.
    """
    def _create_author(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        author = self.model(email=email, **extra_fields)
        author.set_password(password)
        author.save(using=self._db)
        return author

    def create_author(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_author', True)

        return self._create_author(email, password, **extra_fields)


class ReaderManager(BaseUserManager):
    """
     Custom reader manager to create and save a reader with the given email, password and m2m fields.
    """
    def _create_reader(self, email, password, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        # excluding m2m fields
        extra_fields = {field: value for field, value in kwargs.items() if not isinstance(value, list)}

        email = self.normalize_email(email)
        reader = self.model(email=email, **extra_fields)
        reader.set_password(password)
        reader.save(using=self._db)

        # setting m2m fields after saving reader
        reader.liked_posts.set(kwargs.get('liked_posts', []))
        reader.subscribed_authors.set(kwargs.get('subscribed_authors', []))
        reader.subscribed_categories.set(kwargs.get('subscribed_categories', []))

        return reader

    def create_reader(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)

        return self._create_reader(email, password, **kwargs)


class CustomAbstractUser(AbstractUser):
    """
    A custom abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username is rewritten as an email, so manager is changed accordingly.

    Email and password are required. Other fields are optional.
    """
    class Meta:
        abstract = True
        ordering = ['email']

    username = None
    is_author = models.BooleanField(
        _('author'),
        default=False,
        help_text=_(
            'Designates whether this user is author or not'
        ),
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
                         'unique': _("A user with email already exists."),
        },
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    # is_author is required, because by this flag
    # we can figure out what kind of user we should create
    REQUIRED_FIELDS = ['is_author']


class User(CustomAbstractUser):
    """
    Custom User model.

    Email and password are required. Other fields are optional.
    """

    class Meta(CustomAbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Author(User):
    """
    Authors of the blog is represented by this model.

    Image field is optional to use.
    """
    img = models.ImageField(verbose_name="Image of Author", blank=True)
    objects = AuthorManager()

    def __str__(self):
        return self.get_full_name() or self.email


class Reader(User):
    """
    Readers of the blog is represented by this model.

    All fields are optional.
    """
    img = models.ImageField(verbose_name="Image of Reader", blank=True)
    liked_posts = models.ManyToManyField(
        'post.Post',
        verbose_name="Liked posts of a reader",
        related_name="liked_posts",
        related_query_name="liked_readers",
        blank=True
    )
    subscribed_categories = models.ManyToManyField(
        'post.Category',
        verbose_name="Subscribed categories of posts of a reader",
        related_name="subscribed_categories",
        related_query_name="subscribed_readers",
        blank=True
    )
    subscribed_authors = models.ManyToManyField(
        'Author',
        verbose_name="Subscribed authors of a reader",
        related_name="subscribed_authors",
        related_query_name="subscribed_readers",
        blank=True,
    )
    objects = ReaderManager()

    def __str__(self):
        return self.get_full_name() or self.email

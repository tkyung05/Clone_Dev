from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
import uuid

class UserManager(BaseUserManager):

    def create_user(self, email, nickname, password=None, profile_image=None):
        if not email:
            raise ValueError("Users Must Have an email address")
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            profile_image = profile_image,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(email, nickname, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    nickname = models.CharField(
        max_length=50,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    profile_image = models.ImageField(upload_to = 'images/user_profile/%Y/%m/%d')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname',] 

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"
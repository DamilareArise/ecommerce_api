from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **extra_fields):
        
        if email:
            email = self.normalize_email(email)
            try:
                validate_email(email)
            except ValidationError:
                raise ValueError(_("Please enter a valid email address"))
        else:
            raise ValueError(_("An email address is required"))

        
        if not first_name:
            raise ValueError(_("First name is required"))
        
        if not last_name:
            raise ValueError(_("Last name is required"))
        
        
        user = self.model(email=email, first_name=first_name, last_name= last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
        
    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("is staff must be true for admin user"))
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("is superuser must be true for admin user"))

        user = self.create_user(email, first_name, last_name, password, **extra_fields)
        user.save(using = self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
    
    
    

# def hello(params, *bonus, **properties):
#     print(params)
#     print(bonus)
#     print(properties)


# hello('Dami', 'laptop', 'Bottle', size='Big', color='red' )
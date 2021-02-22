from django.db import models
#from django.contrib.auth.models import User

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


#from django.contrib.auth import get_user_model
#User = get_user_model()


class Panchayath(models.Model):
    user_panchayath = models.CharField(max_length=32)
    panchayath_population = models.CharField(max_length=50)
    panchayath_state = models.CharField(max_length=50)
    panchayath_district = models.CharField(max_length=50)
    panchayath_name = models.CharField(max_length=50)


class MyUserManager(BaseUserManager):
    def create_user(self, email, mobile_no, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile_no=mobile_no,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile_no, password=None):
        user = self.create_user(
            email,
            password=password,
            mobile_no=mobile_no,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    mobile_no = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_no']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Person(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='person')
    user_username = models.CharField(max_length=50)
    user_wanumber = models.BigIntegerField()
    user_panchayath = models.CharField(max_length=50)
    user_district = models.CharField(max_length=50)
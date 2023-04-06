from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, username, email, passwoed=None):
        if not email:
            raise ValueError('Enter Email!')
        user = self.model(
            username = username,
            email = email
        )
        user.set_password(passwoed)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    website = models.URLField(null=True)
    picture = models.FileField(null=True)

    USERNAME_FIELD = 'email' #このテーブルのレコードを一意に識別する
    REQUIRED_FIELDS = ['username'] # スーパーユーザー作成時に入力する
    
    objects = UserManager()

    def __str__(self):
        return self.email
    
class Students(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.IntegerField()
    school = models.ForeignKey(
        'Schools', on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'students'

class Schools(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'schools'
from django.db import models
#UD8.1.b
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.

#UD8.1.b

    
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None, type=None):
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username= models.CharField(max_length=30,null=True)
    email=models.EmailField(verbose_name="email address",max_length=255,unique=True)
    activo=models.BooleanField(default=False)
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def str(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app app_label?"
        return True
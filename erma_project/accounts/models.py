from django.db.models import (EmailField , BooleanField , CharField)
from django.contrib.auth.base_user import AbstractBaseUser , BaseUserManager
from django.contrib.auth.hashers import identify_hasher , make_password

class PersonManager(BaseUserManager):

    def create_user(self , email , password = None , **extra_fields):
        if not email:
            raise ValueError("User must have email address.")
        
        user = self.model(email = self.normalize_email(email) , **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self , email , password , **extra_fields):

        extra_fields.setdefault("is_staff" , True)
        extra_fields.setdefault("is_superuser" , True)
        extra_fields.setdefault("is_active" , True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        elif extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_admin=True.")

        return self.create_user(email , password , **extra_fields)


# Create your models here.
class Person(AbstractBaseUser):

    SKILLS = (
        ( "web" , "Web developer") , 
        ( "mobile" , "Mobile app developer")
    )


    name = CharField(max_length = 255)
    email = EmailField(unique = True , max_length = 255)
    is_dev = BooleanField(default = False)
    skills = CharField(max_length = 6 , choices = SKILLS , default = 'web')

    is_staff = BooleanField(default = False)
    is_superuser = BooleanField(default = False)
    is_active = BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name' ,]
    objects = PersonManager()

    def __str__(self):
        return self.name
    
    # it's obligatory 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    def save(self , *args , **kwargs):
        try:
            alg = identify_hasher(self.password)
        except ValueError:
            alg = make_password(self.password)
        super().save(*args , **kwargs)
    
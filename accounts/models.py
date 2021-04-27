from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.forms.fields import BooleanField

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.confirmed_email = False
        user_obj.save()
        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save()
        

class User(AbstractBaseUser):

    TENANT = 1
    MANAGER = 2
    ADMINISTRATOR = 3

    ROLE_CHOICES = (
        (TENANT, "TENANT"),
        (MANAGER,"MANAGER"),
        (ADMINISTRATOR, "ADMINISTRATOR"),
    )

    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=False)  # allows login - set after email confirmation
    staff = models.BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  # superuser
    confirmed_email = models.BooleanField(default=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
   
    # USERNAME_FIELD and password are required by default
    USERNAME_FIELD = 'email'

    objects = UserManager()



    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email 
    
    def get_short_name(self):
        return self.email 
    
    def has_perm(self, perm, obj=None):
        return True 
    
    def has_module_perms(self, app_label):
        return True 

    @property
    def is_admin(self):
        return self.admin 

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

class Country(models.Model):
    name =  models.CharField(max_length=100, blank=True)
    available = models.BooleanField(default=False,null=True, blank=True,)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('name', )
        
    def __str__(self):
        return self.name   

class Profile(models.Model):
    user =   models.OneToOneField(settings.AUTH_USER_MODEL,primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone  = models.CharField(max_length=100,null=True, blank=True, unique=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField(max_length=20000,null=True, blank=True,)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True, blank=True,)
    state = models.CharField(max_length=100,null=True, blank=True,)
    zip_code = models.CharField(max_length=100,null=True, blank=True,)
    signup_confirmation =  models.BooleanField(default=False)

    def email_user(self, *args, **kwargs):
        send_mail(
              'Subject here',
    'Here is the message.',
    ['gilwellm@gmail.com'],
    [self.user.email],
    fail_silently=False,
        )

    def __str__(self):
        return "{} {}".format(self.user.get_username(),self.first_name, self.last_name)
    
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()




    




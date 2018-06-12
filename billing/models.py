from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from accounts.models import GuestEmail
# User contains current instance of the user
User = get_user_model()

# Create your models here.

# Billing Profile manager
class BillingProfileManager(models.Manager):

    def new_or_get(self, request):
        user = request.user
        guest_email_id = request.session.get('guest_email_id')
        created = False
        obj = None
        if user.is_authenticated:
            # logged in user checkout. It remembers payment stuff
            obj, created = self.model.objects.get_or_create(
                user=user, email=user.email)
        elif guest_email_id is not None:
            # guest user checkout. It reloads payment stuff
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            obj, created = self.model.objects.get_or_create(
                email=guest_email_obj.email)
        else:
        	pass
        return obj, created


class BillingProfile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    # auto_now updates time everytime object is saved
    update = models.DateTimeField(auto_now=True)
    # auto_now_add saves time once the object is created
    timestamp = models.DateTimeField(auto_now_add=True)
    # customer id in Stripe or Braintree
    objects = BillingProfileManager()
    def __str__(self):
        return self.email


# def billing_profile_created_receiver(sender, instance, created, *args, **kwrags):
# 	if created:
# 		print('ACTUAL API REQUEST Send to Stripe/Braintree')
# 		instance.customer_id = newID
# 		instance.save()


def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(
            user=instance,	email=instance.email)


post_save.connect(user_created_receiver, sender=User)

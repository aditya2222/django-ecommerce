from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

# User contains current instance of the user
User = get_user_model()

# Create your models here.

class BillingProfile(models.Model):
	user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
	email = models.EmailField()
	active = models.BooleanField(default=True)
	# auto_now updates time everytime object is saved
	update = models.DateTimeField(auto_now=True)
	# auto_now_add saves time once the object is created
	timestamp = models.DateTimeField(auto_now_add=True)
	# customer id in Stripe or Braintree


	def __str__(self):
		return self.email


def user_created_receiver(sender, instance, created, *args, **kwargs):
	if created:
		BillingProfile.objects.get_or_create(user=instance)



post_save.connect(user_created_receiver, sender=User)
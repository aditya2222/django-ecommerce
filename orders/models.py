from django.db import models
from django.db.models.signals import pre_save
from carts.models import Cart
from ecommerce.utils import unique_order_id_generator

# Create your models here.
# Choice tuples (database stored value, displayed value)
ORDER_STATUS_CHOICE =  (
('created',"Created"),
('paid','Paid'),
('shipped','Shipped'),
('refunded','Refunded'),
	)
	
# order_id has to be random, unique

class Order(models.Model):
	order_id = models.CharField(max_length=120, blank=True)
	# billing_profile = 
	# shipping_address =
	# billing_address = 
	cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
	status = models.CharField(max_length=120,default='created', choices=ORDER_STATUS_CHOICE)
	shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

	def __str__(self):
		return self.order_id


# generate the order_id
# generate the order_total


def pre_save_create_order_id(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_id_generator(instance) 
		# since we are using pre_save we donot have to use instance.save()

# wrapping in pre_save to run just before the objects is saved
pre_save.connect(pre_save_create_order_id,sender=Order)
from django.db import models
from customers.models import costomer
from products.models import product

# Create your models here.
class order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,'ORDER_PROCESSED'),
                   (ORDER_DELIVERED,'ORDER_DELIVERED'),
                   (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE) 
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(costomer,on_delete=models.SET_NULL,null=True,related_name='order')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return 'order--{}--{}'.format(self.id,self.owner.user.username)

class orded_item(models.Model):
    product=models.ForeignKey(product, on_delete=models.SET_NULL,null=True,related_name='added_cart')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(order,on_delete=models.CASCADE,related_name='added_item')


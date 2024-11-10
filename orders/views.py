from django.shortcuts import render,redirect
from . models import order,orded_item
from products.models import product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def show_cart(request):
    user=request.user
    costomer=user.costomer_profile
    cart_obj,created=order.objects.get_or_create(
            owner=costomer,
            order_status=order.CART_STAGE
        )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

def remove_item(request,pk):
    item=orded_item.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('show_cart')

def check_out(request):
    if request.POST:
        try:
            user=request.user
            costomer=user.costomer_profile
            total=float(request.POST.get('total'))
            order_obj=order.objects.get(
            owner=costomer,
            order_status=order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message='your order is processed,item will come with in 2 days thankyou'
                messages.success(request,status_message)
            else :
                status_message='your order is not processed'
                messages.error(request,status_message)
        except Exception as e:
                status_message='your order is not processed'
                messages.error(request,status_message)
    return redirect ('show_cart')   
     
@login_required(login_url='account')
def show_orders_page(request):
    user=request.user
    costomer=user.costomer_profile
    order_page=order.objects.filter(owner=costomer).exclude(order_status=order.CART_STAGE)
    context={'orders' :order_page}
    return render(request,'order_page.html',context)     


        
@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        costomer=user.costomer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=order.objects.get_or_create(
            owner=costomer,
            order_status=order.CART_STAGE
        )
        products=product.objects.get(pk=product_id)

        Orded_item,created=orded_item.objects.get_or_create(
            product=products,
            owner=cart_obj,
            
        )
        if created:
            Orded_item.quantity=quantity
            Orded_item.save()
        else:
            Orded_item.quantity=Orded_item.quantity+quantity
            Orded_item.save()
    return redirect('show_cart')
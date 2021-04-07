from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,TemplateView,DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy,reverse
from django.utils import timezone
from django.contrib import auth,messages
from .models import Item,Order,OrderItem,Banner_item
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from . import forms

User=auth.get_user_model()
class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name="/keekers/signup.html"

class BannerVIew(ListView):   #only TemplateView  supports get get_context_data fucntion
    context_object_name="banner_list"
    model=Banner_item
    template_name="index.html"

    # def get_queryset(self):
    #     Items.objects.all

    def get_context_data(self,**kwargs):
        context=super(BannerVIew,self).get_context_data(**kwargs)
        self.cats=Item.objects.values('p_category')

        self.catts={caty['p_category'] for caty in self.cats}
        # print(self.catts)
        self.l=[]
        for self.cat in self.catts:
            self.objs=Item.objects.filter(p_category=self.cat)
            # print(self.cat)
            # print(self.objs)
            self.l.append(self.objs)
        context['Item_list']=self.l
        return context
#
# class HomeVIew(ListView):
#     model=Item
#     template_name="index.html"
#
#

class Product_detailView(DetailView):
    model=Item
    template_name="keekers/product_detail.html"
    def get_context_data(self,**kwargs):
        context=super(Product_detailView,self).get_context_data(**kwargs)
        self.item=get_object_or_404(Item,slug=self.kwargs['slug'])
        self.order_qs=Order.objects.filter(user=self.request.user,ordered=False)
        self.ordered=False
        if(self.order_qs.exists()):
            self.order=self.order_qs[0]
            if(self.order.items.filter(item__slug=self.item.slug).exists()):
                self.ordered=True
                context['item_present']=self.ordered
                return context

            else:
                context['items_present']=self.ordered
                return context


        else:
            context['item_not_present']=self.ordered
        return context



@login_required
def addToCart(request,slug):
    auth_prod=OrderItem.objects.filter(user__id=request.user.id,ordered=False)
    if(auth_prod.exists()):
        item=get_object_or_404(Item,slug=slug)
        print("item:",item)
        if(item.p_total_Item):
            order_item,created=OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False,
            )
            print("order item : ",created)
            order_qs=Order.objects.filter(user=request.user,ordered=False)
            if( order_qs.exists()):
                order=order_qs[0]
                print(order)
                # check if the order item is in the ordered
                if(order.items.filter(item__slug=item.slug).exists()):
                    order_item.quantity+=1
                    order_item.save()
                else:
                    order.items.add(order_item)
            else:
                ordered_date=timezone.now()
                order=Order.objects.create(user=request.user,ordered_date=ordered_date)
                order.items.add(order_item)
    return redirect("keekers:Product_detail", slug=slug)


# def remove_from_cart(request,slug):
#     item=get_object_or_404(Item,slug=slug)
#     order_qs=Order.objects.filter(user=request.user,ordered=False)
#     if(order_qs.exists()):
#         order=order_qs[0]
#         if(order.items.filter(item__slug=item.slug).exists()):
#             order_item=OrderItem.objects.filter(
#             item=item,
#             user=request.user,
#             ordered=False,
#             )[0]
#             order.items.remove(order_item)
#             return redirect("keekers:Product_detail", slug=slug)
#         else:
#             return redirect("keekers:Product_detail", slug=slug)
#
#     else:
#         #add a message saying the user doesnt have an order
#         return redirect("keekers:Product_detail", slug=slug)

class Cart_data(ListView):
    model=OrderItem
    context_object_name="Cart"
    def get(self,*args,**kwargs):
        context=super(Cart_data,self).get(*args,**kwargs)
        context['Cart']=OrderItem.objects.filter(user=self.request.user,ordered=False)
        self.sub_total=0
        self.total_save=0
        self.orders=OrderItem.objects.filter(user__id=self.request.user.id,ordered=False)
        item_prices=[]
        item_dis_prices=[]
        for item in self.orders:
            item_prices.append(item.item.p_price)
            if(item.item.p_discount_price and not item.item.p_discount_price > item.item.p_price):
                item_dis_prices.append(item.item.p_discount_price)
                self.sub_total+=(item.item.p_discount_price*item.quantity)
                self.total_save+=((item.item.p_price*item.quantity)-(item.item.p_discount_price*item.quantity))
            else:
                self.sub_total+=(item.item.p_price*item.quantity)
        ser_context=serializers.serialize("json",OrderItem.objects.all())
        print(item_prices)
        print(item_dis_prices)
        # ser_item=serializers.serialize('json',Item.objects.all())
        context={'CartTotal':self.sub_total,
                'Total_save':self.total_save,
                "orders":ser_context,
                "item_price":item_prices,
                "item_dis_price":item_dis_prices,
                "Orders":self.orders,
                # "get_item_price":item.get_item_price,
                }
        return JsonResponse(context)
class Cart(ListView):
    model=OrderItem
    template_name="keekers/cart.html"
    context_object_name="Cart"
    def get(self,*args,**kwargs):
        context=super(Cart,self).get(*args,**kwargs)
        self.sub_total=0
        self.total_save=0
        self.orders=OrderItem.objects.filter(user__id=self.request.user.id,ordered=False)
        for item in self.orders:
            if(item.item.p_discount_price and not item.item.p_discount_price > item.item.p_price):
                self.sub_total+=(item.item.p_discount_price*item.quantity)
                self.total_save+=((item.item.p_price*item.quantity)-(item.item.p_discount_price*item.quantity))
            else:
                self.sub_total+=(item.item.p_price*item.quantity)
        return context
    # def cart_quantity(self,request,**kwargs):
    #     if(request.method=='GET'):

@login_required
def increment_cart_item(request):
    if(request.method=='GET'):
        slug=request.GET['slug']
        item=get_object_or_404(Item,slug=slug)
        order_item,created=OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)
        order_qs=Order.objects.filter(user=request.user,ordered=False)
        if( order_qs.exists()):
            order=order_qs[0]
            # check if the order item is in the ordered
            if(order.items.filter(item__slug=item.slug).exists()):
                if(order_item.quantity<=5):
                    order_item.quantity+=1
                    order_item.save()
                    #item.p_total_Item-=1            #instock item
                    #item.save()
            else:
                order.items.add(order_item)
        else:
            ordered_date=timezone.now()
            order=Order.objects.create(user=request.user,ordered_date=ordered_date)
            order.items.add(order_item)
        return HttpResponse("increment")

@login_required
def decrement_cart_item(request):
    if(request.method=='GET'):
        print("yes")
        slug=request.GET['slug']
        item=get_object_or_404(Item,slug=slug)
        order_item,create=OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)
        order_qs=Order.objects.filter(user=request.user,ordered=False)
        if(order_qs.exists()):
            order=order_qs[0]
            if(order.items.filter(item__slug=item.slug).exists()):
                if(order_item.quantity>1):
                    order_item.quantity-=1
                order_item.save()
            else:
                order.items.add(order_item)
        else:
            ordered_date=timezone.now()
            order=Order.objects.create(user=request.user,ordered_date=ordered_date)
            order.items.add(order_item)
        return HttpResponse("decrement")
    else:
        print("no")
        return HttpResponse("error")
    # item=get_object_or_404(Item,slug=slug)
    # order_item,created=OrderItem.objects.get_or_create(
    # item=item,
    # user=request.user,
    # ordered=False,
    # )
    # order_qs=Order.objects.filter(user=request.user,ordered=False)
    # if( order_qs.exists()):
    #     order=order_qs[0]
    #     # check if the order item is in the ordered
    #     if(order.items.filter(item__slug=item.slug).exists()):
    #         if(order_item.quantity>1):
    #             order_item.quantity-=1
    #         order_item.save()
    #     else:
    #         order.items.add(order_item)
    # else:
    #     ordered_date=timezone.now()
    #     order=Order.objects.create(user=request.user,ordered_date=ordered_date)
    #     order.items.add(order_item)
    # return redirect("keekers:cart")

class DeleteItem(DeleteView):
    model=OrderItem
    def get_success_url(self):
        return reverse_lazy('keekers:cart')
# class IncrementItem(UpdateView):
#     fields=('quantity',)
#     model=OrderItem
#     template_name="keekers/cart.html"

# class total_cart_item(ListView):
#     model=OrderItem
#     context_object_name="cartItem"
#     template_name="eekers/checkout.html"
class checkoutPage(ListView):
    model=OrderItem
    context_object_name="cartItem"
    template_name="keekers/checkout.html"
    def get_context_data(self,**kwargs):
        context=super(checkoutPage,self).get_context_data(**kwargs)
        Form=forms.checkoutForm()
        context['Form']=Form
        return context

class ProductListview(ListView):
    model=Item
    template_name="keekers/product_list.html"
    context_object_name="item_list"
# class LoginUserView(TemplateView):
#     template_name="keerkers/login.html"

# class CreateUserView(TemplateView):
#     template_name="keerkers/signup.html"

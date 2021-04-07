from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.contrib import auth
# Create your models here.
from django.db.models import Count
from django.urls import reverse_lazy,reverse



User=auth.get_user_model()
CATEGORY_CHOICES=(
    ('NEW ARRIVAL','New Arival'),
    ('R','RayBan'),
    ('P','Polarised'),
    ('T','Titan Eye'),
)
LABEL_CHOICES=(
    ('P','Primary'),
    ('S','Secondary'),
    ('OW','Denger'),

)
GENDER_CHOICES=(
    ('M',"MALE"),
    ("F","FEMALE"),
    ("C","CHILD"),
)
SUB_CATEGORY_CHOICES=(
    ("CLASSIC","CLASSIC EYEGLASSES"),
    ("PREMIUM","PREMIUM EYEGLASSES"),
    ("ECONOMY","ECONOMY EYEGLASSES"),
    ("0 POWER","0 POWER BLUE GLASSES"),
)
FRAME_TYPE_CHOICES=(
    ("REACT","RECTANGLE"),
    ("WAY","WAYFARER"),
    ("ROUND","ROUNDED"),
    ("AVIATOR","AVIATOR"),
    ("CAT-E","CAT-EYE"),
    ("RIM-L","RIMLESS"),
    ("HALF-R","HALF-RIM"),

)
BRAND_CHOICES=(
    ("VINCENT CHASE","VINCENT CHASE"),
    ("JOHN JACOBS","JOHN JACOBS"),
    ("RAY-BAN","RAY-BAN"),
    ("CARRERA","CARRERA"),
    ("OAKLEY","OAKLEY"),
    ("TOMMY HILFIGURE","TOMMY HILFIGURE"),
    ("VOGUE","VOGUE"),

)
class Item(models.Model):
    p_name=models.CharField(max_length=50)
    p_price=models.PositiveIntegerField()
    p_discount_price=models.FloatField(blank=True,null=True)
    p_brand=models.CharField(max_length=50,choices=BRAND_CHOICES,default="VINCENT CHASE")

    p_description=models.TextField(max_length=500)
    p_features=models.TextField(blank=True)
    p_publish_date=models.DateTimeField(auto_now_add=True)
    p_category=models.CharField(choices=CATEGORY_CHOICES,max_length=20,default="N")
    p_sub_category=models.CharField(max_length=100,choices=SUB_CATEGORY_CHOICES,default="CLASSIC")
    p_frame_type=models.CharField(max_length=100,choices=FRAME_TYPE_CHOICES,default="REACT")
    p_style=models.CharField(max_length=100,default="TR FLEX")
    p_gender=models.CharField(max_length=50,choices=GENDER_CHOICES,default="M")
    p_total_Item=models.PositiveIntegerField()
    slug=models.SlugField(allow_unicode=True,unique=True)


    p_image=models.ImageField(upload_to="images/")
    p_image_sub_1=models.ImageField(upload_to="images/", null=True,blank=True)
    p_image_sub_2=models.ImageField(upload_to="images/",null=True,blank=True)
    p_image_sub_3=models.ImageField(upload_to="images/",null=True,blank=True)
    p_image_sub_4=models.ImageField(upload_to="images/",null=True,blank=True)
    p_image_sub_5=models.ImageField(upload_to="images/",null=True,blank=True)
    p_image_sub_6=models.ImageField(upload_to="images/",null=True,blank=True)
    p_image_sub_7=models.ImageField(upload_to="images/",null=True,blank=True)
    p_image_sub_8=models.ImageField(upload_to="images/",null=True,blank=True)
    p_image_sub_9=models.ImageField(upload_to="images/",null=True,blank=True)
    p_image_sub_10=models.ImageField(upload_to="images/",null=True,blank=True)
    def save(self):
        for field in self._meta.fields:
            if field.name == 'p_image':
                field.upload_to = 'images/%s' % self.p_name
        super(Item, self).save()

    def __str__(self):
        return self.p_name
    def get_absolute_url(self):
        return  reverse('keekers:Product_detail', kwargs={'slug':self.slug})
    def get_add_to_cart_url(self):
        return reverse('keekers:addToCart',kwargs={'slug':self.slug})
    def get_remove_from_cart(self):
        return reverse('keekers:removeFromCart',kwargs={'slug':self.slug})
    def get_increment_cart_item_url(self):
        return reverse('keekers:increment_cart_item',kwargs={'slug':self.slug})

class Banner_item(models.Model):
    offText=models.CharField(max_length=50,default="")
    image=models.ImageField(upload_to="images",default="")
    pd_category=models.ForeignKey(Item,related_name="Items",on_delete=models.CASCADE,default="",null=True)
    #
    # def get_absolute_url(self):
    #     return  reverse('product_detail', kwargs={'slug':self.pd_category.slug})
    # def get_queryset(self):
    #     return self.banner_item_set.filter(pd_category=pd_category).count()





class OrderItem(models.Model): #your Original CART
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    ordered=models.BooleanField(default=False)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    total=models.BigIntegerField(default=1)
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    update_on=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.p_name}"

    def get_total_price(self):
        self.total_price=0
        if(self.item.p_discount_price):
            self.total_price+=self.item.p_discount_price*self.quantity
        else:
            self.total_price+=self.item.p_price*self.quantity
        return self.total_price
    def get_absolute_url(self):
        return reverse("keekers:cart")

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()                    # default= "2020-05-30 01:24"
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

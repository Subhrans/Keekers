from django.contrib import admin
from .models import Item,Order,OrderItem,Banner_item
from django.contrib.admin import ModelAdmin
# Register your models here.
class ItemAdmin(ModelAdmin):
    list_display=['p_name','p_publish_date']
    search_fields=['p_name','slug']
    list_per_page=10
    list_filter=['p_publish_date','p_brand','p_category','p_price','p_total_Item']
admin.site.register(Item,ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Banner_item)

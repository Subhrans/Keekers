from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name="keekers"
urlpatterns=[
    path(r'home/',views.BannerVIew.as_view(),name="home"),
    path(r'product_detail/<slug>/',views.Product_detailView.as_view(),name="Product_detail"),
    path(r'login/',
        auth_views.LoginView.as_view(template_name="keekers/login.html"),
        name="login"),
    path(r'logout/',auth_views.LogoutView.as_view(),name="logout"),
    path(r'signup/',views.SignUp.as_view(),name="signup"),
    path(r'Add_to_Cart/<slug>/',views.addToCart,name="addToCart"),
    # path(r'remove_from_Cart/<slug>/',views.remove_from_cart,name="removeFromCart"),
    path(r"cart/",views.Cart.as_view(),name="cart"),
    path(r"cart_data/",views.Cart_data.as_view(),name="cart_data"),
    path(r'increment_cart_item/',views.increment_cart_item,name="increment_cart_item"),
    # path(r'increment_cart_item/<int:pk>/',views.IncrementItem.as_view(),name="increment_cart_item"),
    path(r'decrement_cart_item/',views.decrement_cart_item,name="decrement_cart_item"),
    # path(r'home/',views.total_cart_item.as_view(),name="total_cart_item"),
    path(r'cart_item/<int:pk>/',views.DeleteItem.as_view(),name="deleteItem"),
    path(r'cart/checkout/',views.checkoutPage.as_view(),name="checkout"),
    path(r'All_products/',views.ProductListview.as_view(),name="All_products"),

    # path(r'home/',views.HomeVIew.as_view(),name="home"),
    # path(r'Product_detail/<slug>/',views.Product_detail.as_view(),name="Product_detail"),
]

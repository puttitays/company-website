from django.urls import path
from .views import home_page_view,AboutPageView,window_page_view,payment_view,address_view,swishqrcode_view

urlpatterns = [
path("", home_page_view,name="home"),
path("about/", AboutPageView.as_view(),name="about"),
path("products/", window_page_view,name="window"),
path("payment/", payment_view,name="payment"),
path("payment/swishqrcode/", swishqrcode_view,name="swishqrcode"),
path("address/", address_view,name="address"),

]
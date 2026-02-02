from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Authentication routes
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    # Book routes
    path('', views.book_list, name='book_list'),
    path('books/', views.book_list, name='book_list_alt'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    
    # Cart routes
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:cart_item_id>/', views.update_cart_item, name='update_cart_item'),
    
    # Checkout & Order routes
    path('checkout/', views.checkout, name='checkout'),
    path('order/confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    
    # Rating routes
    path('book/<int:book_id>/rate/', views.add_rating, name='add_rating'),
    
    # Wishlist routes
    path('wishlist/', views.wishlist_view, name='wishlist_view'),
    path('wishlist/add/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    # Account routes
    path('account/', views.account_view, name='account_view'),
    path('account/edit/', views.edit_account, name='edit_account'),
]

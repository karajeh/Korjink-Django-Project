from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('dashboard/', views.the_dashboard, name='dashboard'),
    path('search/', views.search, name = 'search'),
    path('category/<slug:slug>/', views.category, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
] 

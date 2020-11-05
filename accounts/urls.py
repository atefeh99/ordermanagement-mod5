from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name="home"),
    path('user/', views.userPage, name='user_page'),

    path('account/',views.accountSettings, name='account'),
    
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    
    #password reset urls and views
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name= 'accounts/password_reset.html'), 
     name="reset_password"),#as_view is because of this view is a class based view #this url shows us a blank input for email
   
    path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(template_name= 'accounts/password_reset_sent.html'), 
     name="password_reset_done"),#checks that email sent to user
    
    path('reset/<uidb64>/<token>',
     auth_views.PasswordResetConfirmView.as_view(template_name= 'accounts/password_reset_form.html'), 
     name="password_reset_confirm"),#user recieve an email#userid encoded in base 64#token to check that the password is valid
    
    path('reset_password_complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name= 'accounts/password_reset_done.html'), name="password_reset_complete"),#make sure everything is done

]

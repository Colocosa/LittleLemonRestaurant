#define URL route for index() view
from django.urls import path
from . import views
<<<<<<< HEAD
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('message', views.msg),
    path('api-token-auth/', obtain_auth_token)
=======

urlpatterns = [
    path("", views.index, name="index"),
    ("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
>>>>>>> 158c1d284bef6649668e2917c87e124698bc6d72
]
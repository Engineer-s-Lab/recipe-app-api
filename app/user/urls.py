from django.urls import path

from user import views

app_name = 'user' # This app name is used in the reverse function when we create urls

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'), # name is used to identify in the reverse lookup function
    path('token/', views.CreateTokenView.as_view(), name='token')
]

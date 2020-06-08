from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('search/', views.SearchView.as_view(), name='hello'),
    path('user/', views.UserView.as_view())
    #path('api-token-auth/')
]
from django.urls import path
from .views import Index

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='home'),
    # path('home/', Index.as_view(), name='home'),

]
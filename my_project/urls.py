from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path("accounts/", include("allauth.urls")),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('recipes/', include('recipes.urls'))
]

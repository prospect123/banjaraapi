
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact', include('contact.urls')),
    path('terms_conditions', include('terms_conditions.urls')),
    path('privacy_cookie', include('privacy_cookie.urls')),
    path('verifyotp/', include('verification.urls')),

]

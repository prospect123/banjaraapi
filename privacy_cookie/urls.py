from django.contrib import admin
from django.urls import path,include
from privacy_cookie import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cookie',views.CookieModelViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
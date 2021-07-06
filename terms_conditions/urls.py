from django.contrib import admin
from django.urls import path,include
from terms_conditions import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('terms_conditions',views.ccondModelViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
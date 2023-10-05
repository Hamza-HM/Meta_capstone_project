from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item-detail'),
    path('booking/', include(router.urls)),
    path('api-auth-token', obtain_auth_token)
]
# urlpatterns += [static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view(), name='menu-item-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item-detail'),
    path('booking/', include(router.urls)),

]
# urlpatterns += [static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)]
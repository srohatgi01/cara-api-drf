from django.urls import path
# This import is to include 'settings' in the url patterns.
from django.conf import settings
# This is an import for static files. images are also static files.
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user-list')
router.register(r'appointments', AppointmentViewSet, basename='appointments')
# router.register(r'sample', SampleView, basename='sample')

# # Should be uncommented when Zorg's viewsets.Viewset view is used in views.py
# router.register(r'zorgs', ZorgViewSet, basename='zorg-list')

# # This should be used if only viewset based views are used.
# urlpatterns = router.urls

# # Using this because it includes class based urls and viewset based urls.
urlpatterns = [path('zorgs/', ZorgView.as_view(), name='zorg-list'),
               path('ads/<int:pk>/', AdvertismentView.as_view(),
                    name='advertisment-list')] + router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DRF
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    include,
    path
)

# First party
from main.views import MainViewSet
from school.views import StudentsViewSet, TeacherViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

router: DefaultRouter = DefaultRouter(
    trailing_slash=True
)
router.register('main', MainViewSet)
router.register('students', StudentsViewSet)
router.register('teachers', TeacherViewSet)

urlpatterns += [
    path('api/v1/', include(router.urls))
]
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
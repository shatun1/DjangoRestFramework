from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from users.views import UserModelViewSet, UserCustomVueSet
from users.views import UserCustomViewSet
from TODO.views import ProjectModelViewSet, TODOModelViewSet

router = DefaultRouter()
router.register('users', UserCustomViewSet)
router.register('project', ProjectModelViewSet)
router.register('TODO', TODOModelViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
]

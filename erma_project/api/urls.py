from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('projects' , ProjectViewSet , basename='projects')
urlpatterns = router.urls
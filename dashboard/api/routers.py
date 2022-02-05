from dashboard.api.views import FeaturesViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'features', FeaturesViewSet)

urlpatterns = router.urls
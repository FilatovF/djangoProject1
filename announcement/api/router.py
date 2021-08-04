from rest_framework import routers

from announcement.api.views import AnnouncementViewSet

router = routers.DefaultRouter()
router.register(r'announcement', AnnouncementViewSet)

from rest_framework import viewsets
from rest_framework.response import Response

from announcement.api.serializers import AnnouncementShortSerializer, AnnouncementFullSerializer
from announcement.models import Announcement, Visiting


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementShortSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET' and 'pk' in self.kwargs:
            return AnnouncementFullSerializer
        return AnnouncementShortSerializer
    def retrieve(self, request, *args, **kwargs):
        instance:Announcement = self.get_object()
        if self.request.user!=instance.user:
            Visiting.objects.filter(user=self.request.user, announcement=instance).delete()
            Visiting.objects.create(user=self.request.user, announcement=instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
from django.contrib.auth.models import User
from django.db import models




class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zagolovok = models.CharField(max_length=150)
    polniy = models.TextField()

    @property
    def viewed(self)->int:
        return Visiting.objects.filter(announcement=self).count()


class Visiting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)






from django.db import models
from django.conf import settings
from member.models import Characters
# Create your models here.

class CharInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    char = models.ForeignKey(Characters, on_delete=models.CASCADE)
    galeon = models.IntegerField()
    classToken= models.IntegerField()
    searchDone = models.IntegerField()

    class Meta:
        db_table = "charInfo"
        
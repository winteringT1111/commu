from django.db import models

# Create your models here.

class Item(models.Model):
    itemID = models.IntegerField(primary_key=True)
    itemName = models.TextField()
    itemImage = models.TextField()
    itemCategory= models.TextField()
    itemInfo = models.TextField()
    itemPrice = models.IntegerField()

    class Meta:
        db_table = "items"
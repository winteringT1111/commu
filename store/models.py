from django.db import models

# Create your models here.

class Item(models.Model):
    itemID = models.AutoField(primary_key=True)  
    itemName = models.TextField()
    itemEngName = models.TextField()
    itemImage = models.TextField()
    itemCategory= models.TextField()
    itemInfo = models.TextField()
    itemPrice = models.IntegerField()
    show = models.BooleanField()

    class Meta:
        db_table = "items"
        

class Item_magic(models.Model):
    itemID = models.AutoField(primary_key=True)  
    itemName = models.TextField()
    itemImage = models.TextField()
    itemCategory= models.TextField()
    itemType = models.TextField()
    itemInfo = models.TextField()

    class Meta:
        db_table = "items_magic"
        
        
class Potion(models.Model):
    itemID = models.AutoField(primary_key=True)  
    potion = models.TextField()
    potionInfo = models.TextField()
    potionRecipe = models.TextField()
    degree = models.IntegerField()
    discovered = models.BooleanField()
    discoverer = models.TextField(null=True)
    price = models.IntegerField()
    show = models.BooleanField()
    
    class Meta:
        db_table = "potion"
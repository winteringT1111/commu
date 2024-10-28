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
        

class Item_magic(models.Model):
    itemID = models.IntegerField(primary_key=True)
    itemName = models.TextField()
    itemImage = models.TextField()
    itemCategory= models.TextField()
    itemType = models.TextField()
    itemInfo = models.TextField()

    class Meta:
        db_table = "items_magic"
        
        
class Recipe(models.Model):
    itemID = models.IntegerField(primary_key=True)
    potion = models.TextField()
    potionEng = models.TextField()
    potionInfo = models.TextField()
    potionRecipe = models.TextField()
    discovered = models.IntegerField()
    discoverer = models.TextField()
    forSale = models.IntegerField()
    price = models.IntegerField()
    
    class Meta:
        db_table = "recipe"
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
    itemInfo = models.TextField()
    itemDegree = models.IntegerField()
    itemCategory = models.TextField()
    itemCategory2 = models.TextField()

    class Meta:
        db_table = "items_magic"
        
        
class Potion(models.Model):
    itemID = models.AutoField(primary_key=True)  
    potion = models.TextField()
    potionInfo = models.TextField()
    potionRecipe = models.TextField()
    degree = models.IntegerField()
    price = models.IntegerField()
    discovered = models.BooleanField()
    discoverer = models.TextField(null=True)
    
    class Meta:
        db_table = "potion"
        
        
class Cookie(models.Model):
    itemID = models.AutoField(primary_key=True)  
    itemInfo = models.TextField()
    
    
class Scroll(models.Model):
    itemID = models.AutoField(primary_key=True)  
    itemInfo = models.TextField()
    
class Gacha(models.Model):
    itemID = models.AutoField(primary_key=True)  
    itemName = models.TextField()
    itemImage = models.TextField()
    itemCategory = models.TextField()
    itemInfo = models.TextField()
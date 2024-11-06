from django.contrib import admin
from users.models import CharInfo
from member.models import Inventory, Inventory_magic, Characters
from store.models import Item, Item_magic

# Register your models here.
admin.site.register(CharInfo)
admin.site.register(Item)
admin.site.register(Item_magic)
admin.site.register(Inventory)
admin.site.register(Inventory_magic)
admin.site.register(Characters)
# Generated by Django 5.1.1 on 2024-11-13 15:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_magicgift'),
        ('store', '0005_rename_potioninfo_potion_iteminfo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GachaGift',
            fields=[
                ('giftID', models.AutoField(primary_key=True, serialize=False)),
                ('anonymous', models.BooleanField()),
                ('message', models.TextField(null=True)),
                ('itemCount', models.IntegerField()),
                ('orderDate', models.DateField(null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('giver_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gifts_given3', to=settings.AUTH_USER_MODEL)),
                ('itemInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.gacha')),
                ('receiver_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gifts_received3', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'gachagift',
            },
        ),
        migrations.CreateModel(
            name='Inventory_gacha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCount', models.IntegerField()),
                ('itemInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.gacha')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'inventory_gacha',
            },
        ),
        migrations.CreateModel(
            name='Inventory_potion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCount', models.IntegerField()),
                ('itemInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.potion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'inventory_potion',
            },
        ),
    ]

# Generated by Django 5.1.1 on 2024-11-06 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('charID', models.AutoField(primary_key=True, serialize=False)),
                ('charName', models.TextField()),
                ('charEngName', models.TextField()),
                ('charCatchPhrase', models.TextField()),
                ('charPhrase', models.TextField()),
                ('charImageB', models.TextField()),
                ('charImageA', models.TextField()),
                ('charImageP', models.TextField()),
                ('charImageU', models.TextField()),
                ('charCommission', models.BooleanField()),
                ('charCommissionInfo', models.TextField(null=True)),
                ('charImageInfo', models.TextField(null=True)),
                ('charAge', models.IntegerField()),
                ('charGrade', models.IntegerField()),
                ('charSex', models.TextField()),
                ('charHeight', models.IntegerField()),
                ('charWeight', models.IntegerField()),
                ('charBlood', models.TextField()),
                ('charHouse', models.TextField()),
                ('charNationality', models.TextField()),
                ('charKeyword1', models.TextField()),
                ('charKeyword2', models.TextField()),
                ('charKeyword3', models.TextField()),
                ('charPersonality', models.TextField()),
                ('charEtc', models.TextField()),
                ('charWand1', models.TextField()),
                ('charWand2', models.TextField()),
                ('charWand3', models.TextField()),
                ('charWand4', models.TextField()),
                ('charWandInfo', models.TextField(null=True)),
            ],
            options={
                'db_table': 'character',
            },
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('giftID', models.AutoField(primary_key=True, serialize=False)),
                ('anonymous', models.BooleanField()),
                ('message', models.TextField(null=True)),
                ('itemCount', models.IntegerField()),
                ('orderDate', models.DateField(null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('giver_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gifts_given', to=settings.AUTH_USER_MODEL)),
                ('itemInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
                ('receiver_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gifts_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'gift',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCount', models.IntegerField()),
                ('itemInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='Inventory_magic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemCount', models.IntegerField()),
                ('itemInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item_magic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'inventory_magic',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchaseID', models.AutoField(primary_key=True, serialize=False)),
                ('itemCount', models.IntegerField()),
                ('orderDate', models.DateField(null=True)),
                ('itemInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
    ]

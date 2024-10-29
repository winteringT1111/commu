# Generated by Django 5.1.1 on 2024-10-29 02:07

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
                ('charID', models.TextField(primary_key=True, serialize=False)),
                ('charName', models.TextField()),
                ('charEngName', models.TextField()),
                ('charCatchPhrase', models.TextField()),
                ('charPhrase', models.TextField()),
                ('charImage', models.TextField()),
                ('charCommission', models.TextField()),
                ('charImageInfo', models.TextField()),
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
            ],
            options={
                'db_table': 'character',
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
                ('purchaseID', models.IntegerField(primary_key=True, serialize=False)),
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

# Generated by Django 4.2.4 on 2023-09-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_remove_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://kwalityindiancuisine.com/assets/img/food_images/placeholder.png', max_length=500),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='for_user',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='prod_code',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde, rerum, dolorem, iusto sit saepe alias adipisci aliquam aliquid ullam laudantium atque hic. Rerum autem, esse doloremque reprehenderit aliquid iure\xa0aspernatur!', max_length=500),
        ),
    ]

from django.db import models

# Create your models here.

class Item(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=100, default='xyz')
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=500, default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde, rerum, dolorem, iusto sit saepe alias adipisci aliquam aliquid ullam laudantium atque hic. Rerum autem, esse doloremque reprehenderit aliquid iure aspernatur!")
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://kwalityindiancuisine.com/assets/img/food_images/placeholder.png"
    )

    def __str__(self):
        return self.item_name

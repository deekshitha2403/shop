from django.db import models

from Users.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
    discription = models.CharField(max_length=300)
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to="product_image")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username
    


    


from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.name


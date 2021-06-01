from django.db import models

# Create your models here.
class age(models.Model):
    title=models.CharField(max_length=124)
    description=models.TextField(max_length=900)
    img=models.ImageField(upload_to='field',default='https://cdn.pixabay.com/photo/2020/07/06/01/33/forest-5375005__340.jpg')


    def __str__(self):
     return self.title

class Slider_images(models.Model):
    title=models.CharField(max_length=200)
    slide_image=models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title


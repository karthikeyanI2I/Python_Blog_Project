from django.db import models
from django.conf import settings


class BlogData(models.Model):  
    title  = models.CharField(max_length = 120)
    content   = models.TextField(max_length = 3000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_data = models.BinaryField(verbose_name='Image', blank = True, null = True, editable=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="collected_votes")
    createuser =  models.CharField(max_length=100) 
  
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
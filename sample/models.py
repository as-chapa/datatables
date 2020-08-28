from django.db import models

# Create your models here.
class Book(models.Model):
    """本"""
    class Meta:
        db_table = 'book'
    
    title = models.CharField(verbose_name="本のタイトル", max_length=255)
    author = models.CharField(verbose_name="著者", max_length=255)

from django.db import models

# Create your models here.
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.headline
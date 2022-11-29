from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Tag, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

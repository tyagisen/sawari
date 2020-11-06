from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    # description=models.TextField(null=True,blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='blog/', null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "blog"

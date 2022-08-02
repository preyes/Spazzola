from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True) # url amigable
    
    class Meta:
        verbose_name_plural = 'categorias'
        
    def __str__(self):
        return self.name    
        
    
class Product(models.Model):
    
    category = models.ForeignKey(Category, related_name='producto',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='autor', on_delete=models.CASCADE )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default= 'admin')
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)    
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'productos'
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
        
    
    
    
    
        
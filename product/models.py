from django.db import models
from slugify import slugify

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=30,unique=True,verbose_name='Название')
    slug=models.SlugField(max_length=30,primary_key=True,blank=True)


    def __str__(self):
        return self.title


    def save(self,*args,**kwargs):
        if not self.slug:
            self.__slug=slugify(self.title)
            super().save()
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products',verbose_name='Категория')
    title=models.CharField(max_length=50,unique=True,verbose_name='Название')
    slug=models.SlugField(max_length=50,primary_key=True,primary_key=True,blank=True)
    image=models.ImageField(upload_to='products_img/',blank=True,verbose_name='картина')
    description=models.TextField(blank=True,verbose_name='описание')
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='цена')
    qantity=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super()

class ProductImage(models.Model):
    image=models.ImageField(upload_to='products_img/')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')




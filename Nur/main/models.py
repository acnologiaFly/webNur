from django.db import models
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    content=models.TextField(blank=True)
    photo=models.ImageField(upload_to="photos/ProductImages")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'slug'),)
    def get_absolute_url(self):
        return reverse('main:product_detail', kwargs={'product_id': self.pk})

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')


from django.contrib.auth.models import \
    User  # import the default user model of django
from django.db import models
from django.urls import \
    reverse  # reverse is used to return the URL of the category


class ProductManager(models.Manager): #custom model manager
    def get_queryset(self): #returns the products that are in stock
        return super(ProductManager, self).get_queryset().filter(is_active=True) #super() is used to call the get_queryset() method of the parent class (models.Manager)

# each products will have a category
class Category(models.Model): #represents the categories for the products on the store
    name = models.CharField(max_length=255, db_index=True) #name of the category
    slug = models.SlugField(max_length=255, unique=True) #slug is a short label for the category, containing only letters, numbers, underscores or hyphens. It's used in URLs.

    class Meta:
        verbose_name_plural = 'categories' #plural form of category

    #def get_absolute_url(self): #returns the URL of the category
        #return reverse('store:category_list', args=[self.slug])

    def get_absolute_url(self): #returns the URL of the category
        return reverse('store:category_list', args=[self.slug])

    def __str__(self): #returns the name of the category when it's called
        return self.name
    

class Product(models.Model): #represents the products on the store
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) #each product will have a category
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator') #each product will have a creator, User è il default user model di django
    title = models.CharField(max_length=255) #title of the product
    author = models.CharField(max_length=255, default='admin') #author of the product
    description = models.TextField(blank=True) #description of the product
    image = models.ImageField(upload_to='images/', default='images/default.jpg') #image of the product, then I'll create an album table, and each product will have an album
    #we only store the link to he image, not the image itself
    slug = models.SlugField(max_length=255) #slug is a short label for the product, containing only letters, numbers, underscores or hyphens. It's used in URLs.
    price = models.DecimalField(max_digits=10, decimal_places=2) #price of the product
    in_stock = models.BooleanField(default=True) #if the product is in stock or not
    is_active = models.BooleanField(default=True) #if the product is active or not
    created = models.DateTimeField(auto_now_add=True) #when the product was created
    updated = models.DateTimeField(auto_now=True) #when the product was updated
    objects = models.Manager() #default manager
    products = ProductManager() #custom manager

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',) #order the products by the date they were created, the minus sign means descending order, so the most recent products will be displayed first

    def get_absolute_url(self): #returns the URL of the product
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self): #returns the title of the product when it's called
        return self.title
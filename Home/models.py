from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def calculate_total_price(self):
        # Calculate and update the total_price based on OrderItems
        total_price = sum(item.subtotal for item in self.orderitem_set.all())
        self.total_price = total_price
        self.save()

    def __str__(self):
        return str(self.total_price)
    

    def calculate_total_quantity(self):
        # Calculate and return the total quantity based on OrderItems
        total_quantity = sum(item.quantity for item in self.orderitem_set.all())
        return total_quantity
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return str(self.product)

__author__ = 'Muizudeen Kusimo'

from django.db import models

CHK_SALES = (
    (True, 'Yes'),
    (False, 'No'),
)

PLATFORMS = (
    ('android', 'Android Device'),
    ('ios', 'iPhone/iPad'),
    ('web', 'Web'),
)

class Category(models.Model):
    name = models.CharField(max_length=105, help_text="Category Name")
    description = models.CharField(max_length=105, help_text="Description")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

class Designer(models.Model):
    name = models.CharField(max_length=105, help_text="Designer Name")
    description = models.CharField(max_length=105, help_text="Description")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Brand/Design"
        verbose_name_plural = "Brands/Designs"

class Product(models.Model):
    name = models.CharField(max_length=105, help_text='Name of Item')
    category = models.ForeignKey(Category, related_name='product_category', \
               help_text='Category')
    designer = models.ForeignKey(Designer, related_name='product_designer', \
               help_text= 'Designer/Brand Name')
    colour = models.CharField(max_length=15, help_text='Colour of Item')
    price = models.FloatField()
    description = models.CharField(max_length=105, \
                help_text='Product Description')
    #photo =
    last_stocked_timestamp = models.DateTimeField()
    quantity = models.IntegerField(help_text="How many units of this product?")
    on_sales_bool = models.BooleanField(choices=CHK_SALES, help_text="Is this item on Sales/Promo/Discount?")
    entry_by = models.CharField(max_length=105, help_text="Product Added by ...")
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Product/Store Item"
        verbose_name_plural = "Products/Store Items"

class Customer(models.Model):
    firstname = models.CharField(max_length=105, help_text="First Name")
    lastname = models.CharField(max_length=105, help_text="Last Name")
    username = models.CharField(max_length=15, help_text="Username")
    password = models.CharField(max_length=7, help_text="Password")
    mobile_platform = models.CharField(max_length=15, help_text="Mobile Device Platform", \
                                       default="android", choices=PLATFORMS)
    phone_no = models.CharField(max_length=15, help_text="Primary Phone Number", unique=True)
    email = models.EmailField(max_length=105, help_text="Email Address", unique=True)
    date_registered = models.DateTimeField(auto_now_add=True, help_text="Date Registered")

    def __unicode__(self):
        return self.firstname, self.lastname, self.email

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

class Sale(models.Model):
    name = models.CharField(max_length=105, help_text="What event/holiday is this sale for?", default="Sales!!!")
    product = models.ForeignKey(Product, related_name="product_on_sale")
    sale_start_date = models.DateTimeField(auto_now_add=True, help_text="Start Date for Product Sale Period")
    sale_end_date = models.DateTimeField(help_text="When does the Sale end?")
    regular_price = models.FloatField(help_text="Regular Price of Product")
    sale_price = models.FloatField(help_text="Sales/Promo/Discount Price")
    conditions = models.TextField()
    sale_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Discount/Sale"
        verbose_name_plural = "Discounts/Sales"

class Order(models.Model):
    product = models.ForeignKey(Product, related_name="product_ordered", help_text="Product Ordered")
    quantity = models.IntegerField(help_text="Quantity Ordered")
    is_wishlist_bool = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, related_name="ordered_by", help_text="Who ordered this item(s)?")
    order_platform = models.CharField(max_length=55, help_text="Order Platform", choices=PLATFORMS)
    mobile_coord_upon_order = models.CharField(max_length=105, blank=True, null=True, \
                                               help_text="Customer's GPS Coords while ordering")
    order_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.customer

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

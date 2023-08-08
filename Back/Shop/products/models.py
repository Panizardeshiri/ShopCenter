from django.db import models
from django.utils.text import slugify
from accounts.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True,null=True)

    def save(self):
        self.slug = slugify(self.title)

        super(Category, self).save()


    def __str__(self):
        return self.slug



class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True,null=True)
    price=models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    add_to_favorite = models.BooleanField(default=False)
    barnd = models.TextField(blank=True,null=True)
    size = models.TextField(blank=True,null=True, default=1)
    color = models.TextField(blank=True,null=True) 
    exist = models.BooleanField(default=False)
    price_off = models.IntegerField()
    # likes = models.ManyToManyField(User,on_delete=models.CASCADE,related_name='user_likes')

    # def total_likes(self):
    #     return self.likes.count()
    



    def total_price(self):

        total_price = self.price - self.price*self.price_off*0.01

        return total_price
    

    def __str__(self):
        return self.name
    

class Favorit_List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='owner_favorit_list')
    product = models.ManyToManyField(Product,related_name="favorit_product")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner)













class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user)




#  Create Cart Model
class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='owner_cart')
    item = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='item_cart')
    quantity = models.IntegerField(null=True,blank=True)
    

    def cart_tatolprice(self):
    
        cart_totalprice = self.item.total_price()*self.quantity

        return cart_totalprice


    def __str__(self):
       return self.item.name+ '  ' + str(self.quantity)
    


class ShoppingCart(models.Model):
     owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='owner_shoppingcart')
     cart =models.ManyToManyField(Cart)
     is_paid= models.BooleanField(default=False)
     created_at =models.DateTimeField(auto_now_add=True)
     total_price = models.PositiveIntegerField(null=True,blank=True)


     def __str__(self):
       return f"User: {self.owner}"
    

    
















# class CartItems(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='owner_cartitems')
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cart_cartitems')
#     item = models.ForeignKey(Product, on_delete=models.CASCADE)
#     price = models.FloatField(blank=True,null=True)
#     quantity = models.IntegerField(blank=True,null=True)


#     def __str__(self):
#         return str(self.item)











# @receiver(pre_save,sender=CartItems)
# def calculation(sender, **kwargs):
#     cart_items = kwargs['instance'] 

#     each_item = Product.objects.get(id= cart_items.item.id)
#     if each_item.price_off !=0:
#         cart_items.price = cart_items.quantity * (each_item.price - each_item.price * each_item.price_off * 0.01)

#     else:
#         cart_items.price = cart_items.quantity * each_item.price


    

# @receiver(post_save, sender=User)
# def save_cart(sender, instance, created, **kwargs):
#     if created:
#         Cart.objects.create(owner=instance)
    



























    # total_cart_items = CartItems.objects.filter(owner=cart_items.owner)
    # cart = Cart.objects.get(id= cart_items.cart.id)
    # print(cart.cart_totalprice)
    # for cart_items in CartItems.objects.all():
    #     cart.cart_totalprice += cart_items.price
    # cart.cart_totalprice = cart_items.price
    # print(len(total_cart_items))
    # # print(cart.cart_totalprice)
    # cart.cart_totalquantity = len(total_cart_items )
    # print(cart.cart_totalquantity)
    # cart.save






















# class Cart(models.Model):

#     owner = models.ForeignKey(User,related_name='cart_owner',on_delete=models.CASCADE,null=True)
#     item = models.ForeignKey(Product ,related_name='cart_item', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def total_items(self):
#         total_items = 0
#         for item in Cart.objects.all():
#             total_items += item.quantity

#         return total_items

    

#     def item_detail(self):
            
#         print(self.item) 

#         return self.item
    
#     def cart_price(self):
#         cart_price = 0
#         for item in Cart.objects.all():
#             cart_price += item.item.price*item.quantity

#         return cart_price

#     def __str__(self):
#         return f"User: {self.owner}"
    
# class CartItems(models.Model):
#     cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cartitems_cart') 
#     item = models.ManyToManyField(Product,related_name='cartitems_item')  
#     quantity = models.PositiveIntegerField(default=1)
#     item_price = models.FloatField(null=True) 
    







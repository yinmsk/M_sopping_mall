from django.db import models
from user import models as user_models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

    def __str__(self): # admin page에서 name을 보여준다.
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True) # 긴 문자열 필드
    price = models.DecimalField(max_digits=10, decimal_places=2) # 소수점 이하의 숫자를 저장하는 필드
    stock = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=100) # 주문 상태(완료, 취소, 준비, 발송)

    class Meta:
        db_table = 'order_status'

    def __str__(self):
        return self.status_name


class ProductOrder(models.Model): # 유저가 구매한 상품 개수 저장
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)
    product_count = models.IntegerField()

    class Meta:
        db_table = 'product_orders'


class UserOrder(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.SET_NULL, null=True)
    product_order = models.ForeignKey('ProductOrder', on_delete=models.SET_NULL, null=True)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)

    delivery_address = models.CharField(max_length=1000)
    order_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2)

    discount_rate = models.DecimalField(max_digits=20, decimal_places=2)
    final_price = models.DecimalField(max_digits=20, decimal_places=2)

    active = models.BooleanField()

    class Meta:
        db_table = 'user_orders'
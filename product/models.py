from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True) #
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True) # 긴 문자열 필드
    price = models.DecimalField(max_digits=10, decimal_places=2) # 소수점 이하의 숫자를 저장하는 필드
    stock = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self): # admin page에서 name을 보여준다.
        return self.name


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=100) # 주문 상태(완료, 취소, 준비, 발송)

    class Meta:
        db_table = 'order_status'


class ProductOrder(models.Model): # 유저가 구매한 상품 개수 저장
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)
    product_count = models.IntegerField()

    class Meta:
        db_table = 'product_orders'


# 유저의 주문(배송주소, 주문시간, 전체 상품 가격, 할인율, 최종가격, 유효여부(boolean))
# class UserOrder(models.Model):

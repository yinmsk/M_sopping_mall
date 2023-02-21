from django.urls import path
from product import views
'''
class base view 같은 경우는 as_view()가 필요 합니다.
'''

urlpatterns = [
	# product/
	path('', views.ProductView.as_view()),
]
from django.urls import path
from user import views # CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
'''
class base view 같은 경우는 as_view()가 필요 합니다.
'''

urlpatterns = [
	# user/
	path('', views.UserView.as_view(), name="user_view"),
	path('login/', views.UserApiView.as_view()),

	# path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
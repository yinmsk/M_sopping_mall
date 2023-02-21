from django.test import TestCase
from django.urls import reverse # urls.py의 해당 name의 "path()"를 가져와준다.
from rest_framework.test import APITestCase
from rest_framework import status


class UserRegistrationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "email" : "test@testuser.com",
            "password" : "1234",
        }
        '''
        post method를 보낸 url과 user_data의 값들은 변수 response에 저장됩니다.
        그리고 해당 값을 assertEqual() 함수를 통해 status를 확인 및 검증 합니다.
        '''
        response = self.client.post(url, user_data)
        print(url)
        self.assertEqual(response.status_code, 200)
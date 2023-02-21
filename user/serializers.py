from rest_framework import serializers
from user.models import User as UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["email", "password"]

        # password는 보안상의 이유로 보이지 않게 가려주었다.
        # extra_kwargs = {
        #     "password": {"write_only": True}
        # }
    # def create(self, validated_data):
    #     password = validated_data.pop("password", "")
    #     user = UserModel(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #
    #     return user
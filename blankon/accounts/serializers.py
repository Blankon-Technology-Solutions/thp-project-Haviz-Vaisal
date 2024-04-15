from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from accounts.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token["username"] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "password",
            "confirm_password",
            "email",
        )

    def validate(self, value):
        if value.get("password") != value.get("confirm_password"):
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return value

    def create(self, validated_data):
        email = validated_data.get("email")
        user = User.objects.create(
            username=email,
            email=email,
        )

        user.set_password(validated_data.get("password"))
        user.save()
        return user

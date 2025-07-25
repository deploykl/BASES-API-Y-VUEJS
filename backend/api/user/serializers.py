from .models import *
from rest_framework import serializers
from django.conf import settings

# Create your views here.
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = "__all__",

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password2": "Las contraseñas no coinciden"}
            )

        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError(
                {"username": "Este nombre de usuario ya está en uso"}
            )

        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError(
                {"email": "Este correo electrónico ya está en uso"}
            )

        return data

    def create(self, validated_data):
        validated_data.pop(
            "password2"
        )  # Eliminar la confirmación de contraseña antes de crear el usuario
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    dependencia_name = serializers.ReadOnlyField(source="dependencia.name")
    area_name = serializers.ReadOnlyField(source="area.name")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "dni",
            "celular",
            "image",  # Este es el campo real del modelo
            "dependencia_name",
            "is_superuser",
            "area_name",
        ]
        read_only_fields = ["is_superuser"]  # Campos que no se pueden modificar

    def validate_username(self, value):
        # Verificar si el username ya está en uso por otro usuario
        if User.objects.exclude(pk=self.instance.pk).filter(username=value).exists():
            raise serializers.ValidationError("Este nombre de usuario ya está en uso")
        return value

    def validate_email(self, value):
        # Verificar si el email ya está en uso por otro usuario
        if User.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso")
        return value

    def update(self, instance, validated_data):
        # Manejo especial para la imagen si es necesario
        if "image" in validated_data:
            # Eliminar la imagen anterior si existe
            if instance.image and instance.image.name not in [
                "empty.png",
                "empty-male.png",
                "empty-female.png",
            ]:
                instance.image.delete(save=False)
        return super().update(instance, validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(required=True, min_length=8)

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Las contraseñas no coinciden"}
            )
        return data

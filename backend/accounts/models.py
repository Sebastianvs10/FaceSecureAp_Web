# Autor: Jhohan Sebastian Vargas S
# Fecha: 2025-02-25
# Project: FaceSecureApp

from django.contrib.auth.models import AbstractUser
from django.db import models

# Autor: Jhohan Sebastian Vargas
# Project: FaceSecureApp
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_code = models.CharField(max_length=100, unique=True)  # Código del usuario
    name_user = models.CharField(max_length=100)  # Nombre del usuario
    face_data = models.BinaryField(null=True, blank=True)  # Registro facial en formato binario
    role = models.CharField(max_length=10, choices=[('Admin', 'Administrador'), ('User', 'Usuario')], default='User')  # Rol del usuario

    # Redefinir username como opcional
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_code", "name_user", "face_data"]  # Campos requeridos al crear el usuario

    def __str__(self) -> str:
        return self.email

class AccessLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Relaciona con CustomUser
    success = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    distance = models.FloatField(null=True, blank=True)  # Agregar el campo para la distancia

    def __str__(self):
        return f"{self.user} - {self.success} - {self.timestamp}"
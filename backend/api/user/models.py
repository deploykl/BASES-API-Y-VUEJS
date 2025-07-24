from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import default_storage
from api.Choises import GENDER_CHOICES
import uuid
import os
from django.utils.text import slugify


def user_image_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    safe_username = slugify(instance.username)
    new_filename = f"{safe_username}-{uuid.uuid4().hex[:8]}{ext}"  # Combina username y parte del UUID
    return f"users/{instance.id}/{new_filename}"


class User(AbstractUser):
    image = models.ImageField(upload_to=user_image_path, default="img/empty.png", null=True, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Género", null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True, verbose_name="Celular", null=True, blank=True)

    def save(self, *args, **kwargs):
        """Maneja la imagen por defecto para nuevos usuarios"""
        if not self.pk and not self.image:  # Solo para nuevos usuarios sin imagen
            self.set_default_image()
        super().save(*args, **kwargs)

    def set_default_image(self):
        """Establece la imagen por defecto según el género"""
        if self.genero == "F":
            self.image = "img/mujer.png"
        elif self.genero == "M":
            self.image = "img/hombre.png"
        else:
            self.image = "img/empty.png"

    def delete(self, *args, **kwargs):
        """Elimina la imagen del almacenamiento si no es por defecto"""
        try:
            if self.image and not self.image.name.startswith("img/empty"):
                default_storage.delete(self.image.path)
            super().delete(*args, **kwargs)
        except IntegrityError as e:
            print(f"Error al eliminar usuario: {e}")
            raise

from datetime import timezone
from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import default_storage
from api.Choises import GENDER_CHOICES
import uuid
import os
from django.utils.text import slugify
from api.validators import validate_dni, validate_celular
from django.utils.translation import gettext_lazy as _


def user_image_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    safe_username = slugify(instance.username)
    new_filename = f"{safe_username}-{uuid.uuid4().hex[:8]}{ext}"  # Combina username y parte del UUID
    return f"users/{instance.id}/{new_filename}"


class User(AbstractUser):
    image = models.ImageField(
        upload_to=user_image_path, default="img/empty.png", null=True, blank=True
    )
    genero = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        verbose_name="Género",
    )
    dni = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="DNI",
        validators=[validate_dni],
    )
    celular = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Celular",
        validators=[validate_celular],
    )
    distrito = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Distrito"
    )
    departamento = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Departamento"
    )

    # Campos del establecimiento laboral
    # codigo = models.CharField(max_length=8, null=True, blank=True, verbose_name="Código de establecimiento")
    # institucion = models.CharField(max_length=8, null=True, blank=True, verbose_name="Institución")
    # establecimiento = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nombre del establecimiento")
    # departamento_es = models.CharField(max_length=100, null=True, blank=True, verbose_name="Departamento del establecimiento")
    # provincia_es = models.CharField(max_length=100, null=True, blank=True, verbose_name="Provincia del establecimiento")
    # distrito_es = models.CharField(max_length=100, null=True, blank=True, verbose_name="Distrito del establecimiento")
    # disa = models.CharField(max_length=100, null=True, blank=True, verbose_name="DISA de salud")
    # cod_disa = models.CharField(max_length=20, null=True, blank=True, verbose_name="Código DISA")
    # red = models.CharField(max_length=100, null=True, blank=True, verbose_name="Red de salud")
    # cod_red = models.CharField(max_length=20, null=True, blank=True, verbose_name="Código Red")
    # cod_microred = models.CharField(max_length=20, null=True, blank=True, verbose_name="Código Microred")
    # unidad_ejecutora = models.CharField(max_length=100, null=True, blank=True, verbose_name="Unidad Ejecutora")
    # cod_ue = models.CharField(max_length=20, null=True, blank=True, verbose_name="Código Unidad Ejecutora")
    # categoria = models.CharField(max_length=20, null=True, blank=True, verbose_name="Categoría del establecimiento")
    # direccion = models.CharField(max_length=250, null=True, blank=True, verbose_name="Dirección del establecimiento")
    # norte = models.CharField(max_length=100, null=True, blank=True, verbose_name="Dirección del establecimiento")
    # este = models.CharField(max_length=100, null=True, blank=True, verbose_name="Dirección del establecimiento")

    created_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_users",
        verbose_name=_("Creado por"),
    )
    updated_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_users",
        verbose_name=_("Actualizado por"),
    )
    deleted_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deleted_users",
        verbose_name=_("Eliminado por"),
    )
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Fecha de eliminación")
    )

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")
        ordering = ["-date_joined"]

    def delete(self, deleted_by=None, *args, **kwargs):
        self.deleted_by = deleted_by
        self.deleted_at = timezone.now()
        self.is_active = False
        self.save()

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

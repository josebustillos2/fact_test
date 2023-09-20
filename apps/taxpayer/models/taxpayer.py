from django.db import models

# Create your models here.


class Taxpayer(models.Model):
    """Modelo base contribuyente"""

    identification = models.CharField(
        max_length=16,
        verbose_name="identificación",
    )
    full_name = models.CharField(max_length=320, verbose_name="Razón Social")
    code = models.CharField(
        max_length=33,
        blank=True,
        null=True,
        verbose_name="registro único de contribuyente",
    )
    email = models.EmailField(
        max_length=400, verbose_name="correo electrónico", null=True, blank=True
    )
    cellphone = models.CharField(
        max_length=336, blank=True, null=True, verbose_name="número celular"
    )
    phone = models.CharField(
        max_length=136, blank=True, null=True, verbose_name="número fijo"
    )
    address = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="dirección y número de casa",
    )
    is_legal_taxpayer = models.BooleanField(default=False)
    reference = models.CharField(
        max_length=256,
        blank=False,
        null=True,
        verbose_name="Referencia",
    )

    class Meta:
        """Información de la clase"""

        verbose_name = "Contribuyente"
        unique_together = ("identification",)

    def __str__(self):
        return f"{self.full_name}"

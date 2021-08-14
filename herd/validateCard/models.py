from django.db import models

class ValidateCard(models.Model):
    """Modelo para la verificación de número de tarjeta válida"""
    card_number=models.CharField(max_length=20)
    industry_name=models.CharField(max_length=50)
    is_valid_card=models.BooleanField(default=False)

    def __str__(self):
        """retornar cadena representando si es un numero de tarjeta valido o no"""
        return "Card Validated with number <{}>".format(self.card_number)
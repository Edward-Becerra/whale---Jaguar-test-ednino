from rest_framework import serializers

class ValidateCardSerializer(serializers.Serializer):
    """ Serializador para la vista de la validacion del numero de tarjeta""" 
    card_number=serializers.CharField(max_length=20)
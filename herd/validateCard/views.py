from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from validateCard import serializers


class ValidateCardView(APIView):
    """Vista de la api validateCard"""

    serializers_class = serializers.ValidateCardSerializer

    def get(self, request, format=None):
        """Retornar lista de las caracteristicas de la Tarjeta validada"""
        api_view = [
            "Ejercicio API REST Django para validar una tarjeta de credito",
            "mediante el uso del algoritmo de Luhn.",
            "Recibe como entrada el numero de la tarjeta",
            "retorna la franquicia a la que pertenece la tarjeta",
            "y si es valida o no.",
        ]
        return Response({"message": "Validacion tarjeta", "info": api_view})

    def post(self, request):
        """Retorna si el numero de la tarejta ingresado es valido"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            card_number = serializer.validated_data.get("card_number")
            card_number_list = list(card_number.replace(" ", ""))
            first_digit = card_number_list[0]
            check_digit = card_number_list.pop()
            card_number_list.reverse()

            processed_digits = []
            industries = [
                "ISO/TC",
                "Aerolinea",
                "Aerolinea y otros",
                "American Express, JCB o Diners Club",
                "VISA",
                "MasterCard",
                "Discover",
                "Empresas petroleras",
                "Salud o telecomunicaciones",
                "Otros",
            ]
            industry_name = industries[int(first_digit)]

            for index, digit in enumerate(card_number_list):
                if index % 2 == 0:
                    doubled_digit = int(digit)*2
                    if doubled_digit > 9:
                        doubled_digit = doubled_digit - 9
                    processed_digits.append(doubled_digit)
                else:
                    processed_digits.append(int(digit))

            total = int(check_digit) + sum(processed_digits)
            is_valid = bool(total % 10==0)

            message = {
                "Card number": card_number,
                "industry_name": industry_name,
                "is_valid": is_valid,
            }
            return Response({"message": message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

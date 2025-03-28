from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UnitConverter
from .serializers import UnitConverterSerializer

class LengthConvertView(APIView):
    def post(self, request):
        value = float(request.data.get('value', 0))
        from_unit = request.data.get('from_unit')
        to_unit = request.data.get('to_unit')
        
        mile = 0
        match from_unit:
            case "millimeter":
                mile = value / 1609344
            case "centimeter":
                mile = value / 160934.4
            case "meter":
                mile = value / 1609.344
            case "kilometer":
                mile = value / 1.609344
            case "inch":
                mile = value / 63360
            case "foot":
                mile = value / 5280
            case "yard":
                mile = value / 1760
            case "mile":
                mile = value
            case _:
                return Response({"detail": f"Unsupported from unit: {from_unit}"}, status=status.HTTP_400_BAD_REQUEST)

        result = 0
        match to_unit:
            case "millimeter":
                result = mile * 1609344
            case "centimeter":
                result = mile * 160934.4
            case "meter":
                result = mile * 1609.344
            case "kilometer":
                result = mile * 1.609344
            case "inch":
                result = mile * 63360
            case "foot":
                result = mile * 5280
            case "yard":
                result = mile * 1760
            case "mile":
                result = mile
            case _:
                return Response({"detail": f"Unsupported to unit: {to_unit}"}, status=status.HTTP_400_BAD_REQUEST)
            
        data = {
            "from_unit": from_unit,
            "to_unit": to_unit,
            "value": value,
            "convert_type": "Length",
            "result": result
        }
        serializer = UnitConverterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeightConvertView(APIView):
    def post(self, request):
        value = float(request.data.get('value', 0))
        from_unit = request.data.get('from_unit')
        to_unit = request.data.get('to_unit')

        pound = 0
        match from_unit:
            case "milligram":
                pound = value / 453592
            case "kilogram":
                pound = value * 2.20462
            case "gram":
                pound = value / 453.592
            case "ounce":
                pound = value / 16
            case "pound":
                pound = value
            case _:
                return Response({"detail": f"Unsupported from unit: {from_unit}"}, status=status.HTTP_400_BAD_REQUEST)

        result = 0
        match to_unit:
            case "milligram":
                result = pound * 453592
            case "kilogram":
                result = pound / 2.20462
            case "gram":
                result = pound * 453.592
            case "ounce":
                result = pound * 16
            case "pound":
                result = pound
            case _:
                return Response({"detail": f"Unsupported to unit: {to_unit}"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save to database
        data = {
            "from_unit": from_unit,
            "to_unit": to_unit,
            "value": value,
            "convert_type": "Weight",
            "result": result
        }
        serializer = UnitConverterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TemperatureConvertView(APIView):
    def post(self, request):
        value = float(request.data.get('value', 0))
        from_unit = request.data.get('from_unit')
        to_unit = request.data.get('to_unit')

        celsius = 0
        match from_unit:
            case "kelvin":
                celsius = value - 273.15
            case "fahrenheit":
                celsius = (value - 32) * 5 / 9
            case "celsius":
                celsius = value
            case _:
                return Response({"detail": f"Unsupported from unit: {from_unit}"}, status=status.HTTP_400_BAD_REQUEST)

        result = 0
        match to_unit:
            case "kelvin":
                result = celsius + 273.15
            case "fahrenheit":
                result = celsius * 9 / 5 + 32
            case "celsius":
                result = celsius
            case _:
                return Response({"detail": f"Unsupported to unit: {to_unit}"}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "from_unit": from_unit,
            "to_unit": to_unit,
            "value": value,
            "convert_type": "Temperature",
            "result": result
        }
        serializer = UnitConverterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
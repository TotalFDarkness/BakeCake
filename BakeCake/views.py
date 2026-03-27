from django.shortcuts import render
from .models import (
    Cake,
    Layer,
    Shape,
    Topping,
    Berry,
    Decor,
    Inscription,
)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    LayerSerializer, ShapeSerializer, ToppingSerializer,
    BerrySerializer, DecorSerializer, InscriptionSerializer
)


def index(request):
    cakes = Cake.objects.filter(default=True)
    layers = Layer.objects.all()
    shapes = Shape.objects.all()
    toppings = Topping.objects.all()
    berries = Berry.objects.all()
    decors = Decor.objects.all()

    context = {
        'cakes': cakes,
        'layers': layers,
        'shapes': shapes,
        'toppings': toppings,
        'berries': berries,
        'decors': decors,
    }
    return render(request, "index.html", context)


def lk(request):
    return render(request, "lk.html")


@api_view(['GET'])
def get_cake_data(request):
    try:
        # Получаем данные из БД
        layers = Layer.objects.all()
        shapes = Shape.objects.all()
        toppings = Topping.objects.all()
        berries = Berry.objects.all()
        decors = Decor.objects.all()
        words_price_obj = Inscription.objects.get(title="Цена надписи")

        data = {
            'layers': LayerSerializer(layers, many=True).data,
            'shapes': ShapeSerializer(shapes, many=True).data,
            'toppings': ToppingSerializer(toppings, many=True).data,
            'berries': BerrySerializer(berries, many=True).data,
            'decors': DecorSerializer(decors, many=True).data,
            'words_price': words_price_obj.price,
        }

        return Response(data, status=status.HTTP_200_OK)

    except Inscription.DoesNotExist:
        return Response(
            {'error': 'Цена надписи не найдена'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

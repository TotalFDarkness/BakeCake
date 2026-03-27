from rest_framework import serializers
from .models import Layer, Shape, Topping, Berry, Decor, Inscription


class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = ['quantity', 'price']


class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = ['id', 'shape', 'price']


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id', 'title', 'price']


class BerrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Berry
        fields = ['id', 'title', 'price']


class DecorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decor
        fields = ['id', 'title', 'price']


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = ['id', 'title', 'price']
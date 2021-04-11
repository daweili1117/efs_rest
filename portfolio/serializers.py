from rest_framework import serializers
from .models import Customer, Investment, Stock
from rest_framework import serializers
from .models import Customer, Investment, Stock, Fund


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'name','cust_number',  'address', 'city', 'state', 'zipcode', 'email', 'email', 'cell_phone')


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = (
        'pk', 'customer', 'cust_number', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value', 'recent_date')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('pk', 'customer', 'cust_number', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date')

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ('pk', 'customer', 'cust_number', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date')
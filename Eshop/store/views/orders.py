from django.views import View
from django.shortcuts import render, redirect
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render (request, 'orders.html', {'orders':orders})



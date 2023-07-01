from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Menu,Booking
from .serializers import MenuItemSerializer,BookingSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authentication import TokenAuthentication

# Create your views here.


def sayHello(request):
    return HttpResponse("Hello Django!")

def index(request):
    return render(request,'index.html',{})

class MenuItemsView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

@api_view()
@permission_classes([IsAuthenticated])

def msg(request):
    return HttpResponse({"message":"This View is Protected"})

class BookingViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer




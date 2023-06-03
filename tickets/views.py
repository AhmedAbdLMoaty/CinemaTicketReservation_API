from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import Guest, Movie, Reservation
from rest_framework.decorators import api_view 
from .serializers import GuestSeriallizer, MovieSerializer, ReservationSerializer
from rest_framework import status , filters
from rest_framework.response import Response
# Create your views here.

#1 without REST and no model query FBV

def no_rest_no_model(request):

    guests = [
        {
            'id': 1,
            'Name': 'omar',
            'mobile': 1233,
        },
        {
            'id': 2,
            'name': 'yassin',
            'mobile': 464564,
        }
    ]
    return JsonResponse ( guests, safe = False)

#2 model data defult django without rest

def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guest': list(data.values('name', 'mobile'))
    }
    return JsonResponse(response)

# list == GET
# Create == POST
# pk query == GET
# Update == PUT
# Delete destory = DELETE

#3 Function based views
# 3.1 GET POST
@api_view(['GET', 'POST'])
def FBV_List(request):
    #GET
    if request.method =='GET': 
        guests = Guest.objects.all()
        serializer = GuestSeriallizer(guests, many = True)
        return Response(serializer.data)
    #POST
    elif request.method =='POST':
        serializer =GuestSeriallizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED) 
        return Response(serializer.data , status.HTTP_400_BAD_REQUEST)
    


# 3.1 GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(  request ,pk ):
    guest = Guest.objects.get(pk=pk)
    try: 
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method =='GET': 
        serializer = GuestSeriallizer(guest)
        return Response(serializer.data)
    #PUT
    elif request.method =='PUT':
        serializer =GuestSeriallizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_406_NOT_ACCEPTABLE) 
        return Response(serializer.errors , status.HTTP_400_BAD_REQUEST)
    #DELETE
    if request.method =='DELETE': 
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from .models import UserAuth
from django.core.serializers import serialize
from django.contrib.auth import authenticate
from pathlib import Path
import json
# Create your views here.
BASE_DIR = "http://127.0.0.1:8000"
class UserAuthView(View):
    def get(self, request):
        data = {
            "status": "error",
            "messege": "GET method is not allowed!",
            }
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
        except:
            data = ''
        if not data:
            data = {
                "status": "error",
                "messages": "username and password are required!"
                }
            return JsonResponse(data, safe=False)
        username = data.get("username")
        password = data.get("password")
        if username == '' or password == '' or username== None or password==None:
            data = {
                "status": "error",
                "messages": "username and password are required!"
                }
            return JsonResponse(data, safe=False)
        user = authenticate(username = username, password = password)
        if user is not None:
            queryset = UserAuth.objects.get(username=username)
            username = queryset.username
            first_name = queryset.first_name
            last_name = queryset.last_name
            email = queryset.email
            phone = queryset.phone
            profile_pic = queryset.profile_pic
            average_rating = queryset.average_rating
            sponsor_id = queryset.sponsor_id

            data = {
                "status": "success",
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "full_name": first_name+' '+last_name,
                "email": email,
                "phone": phone,
                "profile_pic": str(BASE_DIR)+'/'+str(profile_pic),
                "average_rating": average_rating,
                "sponsor_id": sponsor_id
            }
            return JsonResponse(data, safe=False,status=200)
        else:
            data = {
            "status": "error",
            "messages": "Invalid username or password!",
            }
            return JsonResponse(data, safe=False)




















# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# @api_view(['GET'])
# def my_view(request):
#     data = {
#         "message": "Hello, World!",
#         "status": "success",
#         "items": ["item1", "item2", "item3"]
#     }
#     return Response(data)







# from django.http import JsonResponse
# from .models import MyModel
# from django.core.serializers import serialize

# def my_view(request):
#     queryset = MyModel.objects.all()
#     data = serialize("json", queryset)
#     return JsonResponse(data, safe=False)
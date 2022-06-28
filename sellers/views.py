from django.shortcuts import render
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from . models import Shop
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext as _


cloudinary.config(
    cloud_name="dncmqoyt4",
    api_key=632767996739336,
    api_secret='qalqiJvc-LouZEvgKv4bvyeptcQ')

def index(request):
      
     shops =  Shop.objects.filter(user_id=request.user.id) 
     return render(request, "sellers/index.html", {'shops':shops, "hello":_("hello")})

def create_shop(request):
   if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]

        r = cloudinary.uploader.upload(request.FILES["logo"])
        img_url = r["secure_url"]

        Shop(name=name, description=description, logo=img_url, user_id=request.user.id).save()

        return HttpResponseRedirect("/seller/")

   else:
        return render(request, "sellers/create_shop.html")

class FileFieldForm(forms.Form):
     file_field = forms.FileField(widget=forms.ClearableFileInput )

def add_item(request, store_id):
     if request.method == "POST":
          pass
     else:
          images_upload_form = FileFieldForm()
          
          return render(request, "sellers/add_item.html",{'images_upload_form':images_upload_form})
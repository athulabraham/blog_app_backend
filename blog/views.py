from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from blog.serializer import BlogSerializer,UserSerializer
from blog.models import BlogModel,UserModel
from django.db.models import Q


# Create your views here.

    
    
@csrf_exempt
def View(request):
    if request.method=="POST":
       blogLists=BlogModel.objects.all()
       serializer_data=BlogSerializer(blogLists,many=True)
       return HttpResponse(json.dumps(serializer_data.data))
    
    
@csrf_exempt
def Add(request):
    if request.method=="POST":
        recieve_data=json.loads(request.body)
        print(recieve_data)
        serializer_check=BlogSerializer(data=recieve_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"adding"}))
        else:
            return HttpResponse(json.dumps({"status":"false"}))
    
    
    
@csrf_exempt
def Search(request):
    if request.method=="POST":
        recieve_data=json.loads(request.body)
        getTitle=recieve_data["title"]
        data=list(BlogModel.objects.filter(Q(title__icontains=getTitle)).values())
        return HttpResponse(json.dumps(data))
    
    
@csrf_exempt
def Delete(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"hello"}))
    
    


@csrf_exempt
def User(request):
    if request.method=="POST":
        recieve_data=json.loads(request.body)
        print(recieve_data)
        serializer_check=UserSerializer(data=recieve_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"ADD"}))
        else:
            return HttpResponse(json.dumps({"status":"false"}))
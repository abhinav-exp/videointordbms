from django.shortcuts import render
from .models import VideoModel, Foo
from django.http import HttpResponse
from django.http import FileResponse


# Create your views here.
def index(request):
    path = r'testviedo.mp4'

    obj = VideoModel()
    obj.np_field.name = path
    obj.save()
    
    return HttpResponse("hello index")

def fooview(request):
    obj = Foo()

    with open('./testviedo.mp4', 'rb') as f:
        obj.set_data(f.read())
        obj.save()

    return HttpResponse("hello foo " + str(obj.id))
    
def fooret(request, id):
    obj = Foo.objects.get(id = id)

    response = obj.get_data()
    print(type(response))
    
    return HttpResponse(response, content_type='video/mp4')

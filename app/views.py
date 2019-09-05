from django.shortcuts import render
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse 
from django.http import StreamingHttpResponse
from app import models
from app.models import Article
import json
import uuid

# Create your views here.
def index(request):
    article_list = Article.objects.all()
    return render(request,'index.html',{'article_list': json.dumps(article_list,cls = DjangoJSONEncoder)})

def write_server(request):
    data = json.loads(request.body)
    # 生成基于时间的uuid
    data['id'] = uuid.uuid4()
    models.Person.objects.create(**data)
    res = {
        'success' : True
    }

    return HttpResponse(json.dumps(res),content_type = 'application/json')

def get_person(request):
    data = serializers.serialize('python',models.Person.objects.all())
    res = {
        'success' : True,
        'data' : data
    }
    return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder),content_type='application/json')

def get_video_stream(request):
    return StreamingHttpResponse(hello)

def hello():
    yield 'hello,'    
    yield 'there!'
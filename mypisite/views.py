from django.shortcuts import render
from django.http import HttpResponse

def validation(request):
    f = open('/home/rj7/mypisite/validation-key.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

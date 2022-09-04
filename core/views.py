from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework                     import generics

# Create your views here.

class StreamAuth(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello')

    def post(self, request, *args, **kwargs):
        print('1:',request.data)
        print('2:', args)
        print('3:', kwargs)
        return HttpResponse('What?')

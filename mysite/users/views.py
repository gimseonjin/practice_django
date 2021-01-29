from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        userId = request.GET.get('id', None)
        return HttpResponse("GET method " + str(userId))

    def post(self, request):
        return HttpResponse("GET method")

    def put(self, request):
        return HttpResponse("GET method")

    def delete(self, request):
        return HttpResponse("GET method")

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . models import article
from . serializers import articleserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Create your views here.

# model view set


class ModelViewSet(viewsets.ModelViewSet):
    serializer_class = articleserializer
    queryset = article.objects.all()


# generic view set
# class ArticalGenericViewSet(viewsets.GenericViewSet,
#                             mixins.ListModelMixin, mixins.CreateModelMixin,
#                             mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = articleserializer
#     queryset = article.objects.all()


# view-sets and routers
# class articleviewset(viewsets.ViewSet):
#     def list(self, request):
#         Article = article.objects.all()
#         serializer = articleserializer(Article, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = articleserializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = article.objects.all()
#         Article = get_object_or_404(queryset, pk=pk)
#         serializer = articleserializer(Article)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         Article = article.objects.get(pk=pk)
#         serializer = articleserializer(Article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# generic views
# class genericapiview(generics.GenericAPIView, mixins.ListModelMixin,
#                      mixins.CreateModelMixin, mixins.UpdateModelMixin,
#                      mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = articleserializer
#     queryset = article.objects.all()

#     lookup_field = 'id'
#     #authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id=None):
#         return self.update(request, id)

#     def delete(self, request, id):
#         return self.destroy(request, id)

# class based view
# class articleapiview(APIView):

#     def get(self, request):
#         articles = article.objects.all()
#         serializer = articleserializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = articleserializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class articledetails(APIView):

#     def get_object(self, id):
#         try:
#             return article.objects.get(id=id)
#         except article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = articleserializer(article)
#         return Response(serializer.data)

#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = articleserializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# function based view
# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = article.objects.all()
#         serializer = articleserializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = articleserializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     try:
#         Article = article.objects.get(pk=pk)
#     except article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = articleserializer(Article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = articleserializer(Article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     elif request.method == 'DELETE':
#         Article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

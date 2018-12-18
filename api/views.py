from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Document
from .serializer import DocumentSerializer

class ListDocs(APIView):

    def get(self, request):
        docs = Document.objects.all()
        docs_json = DocumentSerializer(docs, many=True)
        return Response(docs_json.data)

    def post(self, request):
        docs_json = DocumentSerializer(data=request.data) #UnMarshall
        if docs_json.is_valid():
            docs_json.save()
            return Response(docs_json.data, status=201)
        return Response(docs_json.errors, status=400)


class DetailDocs(APIView):
    def get_object(self, pk):
        try:
            return Document.objects.get(id=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        docs = self.get_object(pk)
        docs_json = DocumentSerializer(docs)
        return Response(docs_json.data)

    def put(self, request, pk):
        docs = self.get_object(pk)
        docs_json = DocumentSerializer(docs, data=request.data)
        if docs_json.is_valid():
            docs_json.save()
            return Response(docs_json.data)
        return Response(docs_json.errors, status=400)

    def delete(self, request, pk):
        docs = self.get_object(pk)
        docs.delete()
        return Response(status=204)
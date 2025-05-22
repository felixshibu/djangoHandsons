from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InventoryModel
from .serializer import InventorySerializer

# Create your views here.

class InventoryList(APIView):
    def get(self,request):
        items = InventoryModel.objects.all()
        serializer = InventorySerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        barcode = request.data.get('barcode')
        if InventoryModel.objects.filter(barcode=barcode).exists():
            return Response({"error":"inventory with this barcode already exists"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = InventorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class InventoryDetails(APIView):
    def get(self,request,pk):
        try:
            item = InventoryModel.objects.get(pk=pk)
            serializer = InventorySerializer(item)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        item = InventoryModel.objects.get(pk=pk)
        serializer = InventorySerializer(item,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        item = InventoryModel.objects.get(pk=pk)
        item.delete()
        return Response([],status=status.HTTP_204_NO_CONTENT)

class InventoryQuery(APIView):
    def get(self,request,category):
        items = InventoryModel.objects.filter(category=category)
        serializer = InventorySerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class InventorySort(APIView):
    def get(self,request):
        items = InventoryModel.objects.all().order_by('-price')
        serializer = InventorySerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

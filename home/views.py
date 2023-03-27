from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializers import PeopleSerializer


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request):
    courses = {
        'name': 'Django',
        'price': 100,
        'learn': ['python', 'django', 'rest api'],
        'duration': '3 months'
    }

    if request.method == 'POST':
        # print("hitting post", request.data) #used to get data from client
        # print("hitting post method")
        return Response({'message': 'POST Data received', 'data': courses})
    elif request.method == 'GET':
        # print(request.GET.get('search')) #used to searching data from client
        # print("hitting get method")
        return Response({'message': 'GET Data getiing', 'data': courses})
    elif request.method == 'PUT':
        # print("hitting put method")
        return Response({'message': 'PUT Data updated', 'data': courses})
    elif request.method == 'DELETE':
        # print("hitting delete method")
        return Response({'message': 'DELETE Data deleted', 'data': courses})
    

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)   
    
    elif request.method == 'POST':
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors) 
    
    elif request.method == 'PUT':
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors) 
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors) 
    
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Person deleted'})
    





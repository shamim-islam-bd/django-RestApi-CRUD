from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        # print("hitting post method")
        return Response({'message': 'POST Data received', 'data': courses})
    elif request.method == 'GET':
        # print("hitting get method")
        return Response({'message': 'GET Data getiing', 'data': courses})
    elif request.method == 'PUT':
        # print("hitting put method")
        return Response({'message': 'PUT Data updated', 'data': courses})
    elif request.method == 'DELETE':
        # print("hitting delete method")
        return Response({'message': 'DELETE Data deleted', 'data': courses})
    

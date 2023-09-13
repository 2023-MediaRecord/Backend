# login_api/views.py

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, Record_List, Record
from .serializers import UserSerializer

# login_api/views.py

from rest_framework import generics

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def login(request):
    id = request.data.get("user_id")
    password = request.data.get('user_pw')
    print(id)
    if(id):
        user = User.objects.filter(user_id = id)
        
        if(user):
            if(user[0].user_pw == password):
                return Response(status=200, data={"id": user[0].id})
            else:
                return Response({"error": "잘못된 password입니다."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "가입되지 않은 id입니다."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def record_list(request):
    user = request.data.get("user")
    tag = request.query_params.get("tag")

    if(user):
        records = Record_List.objects.filter(owner_id = user)
        
        data = []
        for i in records:
            record = Record.objects.get(pk = i.record_id_id)

            if(tag == '0'):
                data.append(
                    {
                        "id" : record.id,
                        "title" : record.title,
                        "cover_path" : record.cover_path,
                        "isLiked" : record.liked,
                        "tag": record.tag,
                        "date": record.date
                    }
                )
            else:
              if(str(record.tag) == tag):
                  data.append(
                      {
                          "id" : record.id,
                          "title" : record.title,
                          "cover_path" : record.cover_path,
                          "isLiked" : record.liked,
                          "tag": record.tag,
                          "date": record.date
                      }
                  )

        return Response(status=200, data=data)



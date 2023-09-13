from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Record_List, Record, Wish_Media_List, Wish_Media
from .serializers import UserSerializer
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
    print('run record_list')
    user = request.data.get("user")
    tag = request.query_params.get("tag")

    if(user):
        records = Record_List.objects.filter(owner_id = user)
        
        data = []
        for record in records:
            record_data = Record.objects.get(pk = record.record_id_id)

            if(tag == '0'):
                data.append(
                    {
                        "id" : record_data.id,
                        "title" : record_data.title,
                        "cover_path" : record_data.cover_path,
                        "isLiked" : record_data.liked,
                        "tag": record_data.tag,
                        "date": record_data.date
                    }
                )
            else:
              if(str(record_data.tag) == tag):
                  data.append(
                      {
                          "id" : record_data.id,
                          "title" : record_data.title,
                          "cover_path" : record_data.cover_path,
                          "isLiked" : record_data.liked,
                          "tag": record_data.tag,
                          "date": record_data.date
                      }
                  )

        return Response(status=200, data=data)


@api_view(['GET'])
def record(request, record_id):
    
    record = Record.objects.get(pk=record_id)

    res = {
        "title": record.title,
        "tag": record.tag,
        "cover_path": record.cover_path,
        "score": record.score,
        "memo": record.memo,
        "isLiked": record.liked,
        "date": record.date
    }
    
    return Response(status=200, data=res)

@api_view(['GET'])
def mypage(request):
    user_id = request.data.get('user')

    user = User.objects.get(pk=user_id)
    records = Record_List.objects.filter(owner_id = user)
    total = len(records)

    res = {
        "nickname": user.nickname,
        "total": total
    }
    
    return Response(status=200, data=res)

@api_view(['GET'])
def wish_medias(request):
    user_id = request.data.get('user')

    wish_medias = Wish_Media_List.objects.filter(owner_id = user_id)

    data = []
    for media in wish_medias:
        wish_media = Wish_Media.objects.get(pk=media.wish_id_id)

        data.append({
            "id": wish_media.pk,
            "title": wish_media.title,
            "memo": wish_media.memo,
            "tag": wish_media.tag
        })
    
    return Response(status=200, data=data)

        
@api_view(['GET'])
def liked_medias(request):
    user_id = request.data.get('user')

    records = Record_List.objects.filter(owner_id=user_id)

    data = []
    for record in records:
        record_data = Record.objects.get(pk=record.record_id_id)
        
        if(record_data.liked):
            data.append({
                "id" : record_data.id,
                "title" : record_data.title,
                "cover_path" : record_data.cover_path,
                "isLiked" : record_data.liked,
                "tag": record_data.tag,
                "date": record_data.date
            })
    
    return Response(status=200, data=data)

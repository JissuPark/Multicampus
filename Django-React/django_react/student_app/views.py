from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializer import Stdserializer


@api_view(['GET', 'POST'])
def std_list_create(req):
    # GET 방식은 조회
    if req.method == 'GET':
        print(f'In list GET: request data = ({req.data})')
        queryset = Student.objects.all()
        serializer = Stdserializer(queryset, many=True)
        return Response(serializer.data)

    # POST 방식은 생성
    elif req.method == 'POST':
        print(f'In list POST : request data = ({req.data})')
        serializer = Stdserializer(data=req.data)
        # 요청 검증
        if serializer.is_valid():
            # 검증 후 저장하고 post니까 201로 created 보냄
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 검증이 안되면 request가 잘못된거니 400에러 보냄
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def std_details(req, pk):

    # 일단 request가 오면 model에서 pk로 찾는다.
    try:
        student = Student.objects.get(pk=pk)

    # 없으면 not found 404 error를 보낸다.
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # 있으면 아래 내용중 맞는 걸 실행
    # 특정 학생 조회
    if req.method == 'GET':
        print(f'In detail GET : request pk = ({pk})')
        serializer = Stdserializer(student)
        return Response(serializer.data)


    # 학생 정보 수정
    elif req.method == 'PUT':
        print(f'In detail PUT : request data = ({req.data})')
        serializer = Stdserializer(student, data=req.data)
        # 학생 정보가 있으면 검증 후 저장 ==> 업데이트
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # 학생 정보가 없으면 bad request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 학생 정보 삭제
    elif req.method == 'DELETE':
        print(f'In detail DELETE : request data = ({req.data})')
        student.delete()
        # 삭제 후 내용이 없다는 204 반환
        return Response(status=status.HTTP_204_NO_CONTENT)
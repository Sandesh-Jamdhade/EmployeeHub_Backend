from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def login_api(request):
    username = request.data.get("username")

    try:
        user = User.objects.get(username=username)

        print("LOGGED USER:", user.username)
        print("IS SUPERUSER:", user.is_superuser)

        return Response({
            "success": True,
            "is_admin": user.is_superuser
        })

    except User.DoesNotExist:
        return Response({"success": False}, status=401)

@api_view(['POST'])
def register_api(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Missing fields"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=400)

    user = User.objects.create_user(
        username=username,
        password=password
    )

    return Response({"success": True})


@api_view(['GET'])
def is_admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return Response({"is_admin": True})

    return Response({"is_admin": False})

@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def employee_create(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)



@api_view(['GET'])
def employee_detail(request, id):
    emp = Employee.objects.get(id=id)
    serializer = EmployeeSerializer(emp)
    return Response(serializer.data)


@api_view(['PUT'])
def employee_update(request, id):
    emp = Employee.objects.get(id=id)
    serializer = EmployeeSerializer(emp, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)



@api_view(['DELETE'])
def employee_delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return Response({"message": "Deleted"})

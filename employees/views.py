from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer


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

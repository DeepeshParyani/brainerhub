from rest_framework import serializers

from employee.models import Employee


class CompanySerializer(serializers.Serializer):
    companies = serializers.ListField(child=serializers.CharField(max_length=255))


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name', 'phone_number', 'salary', 'manager_id', 'department_id',
                  'company']

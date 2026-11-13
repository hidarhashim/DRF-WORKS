
from django.db.models import Model
from rest_framework import serializers
from app.models import Employee

# class EmployeeSerializer(serializers.Serializer):
#     gender_choices=(('male','Male'),('female','Female'))
#     id=serializers.IntegerField(read_only=True)
#     empid=serializers.IntegerField()
#     name=serializers.CharField(max_length=20)
#     age=serializers.IntegerField()
#     gender=serializers.ChoiceField(choices=gender_choices)
#     salary=serializers.IntegerField()
#     designation=serializers.CharField(max_length=20)
#     joining_year=serializers.DateField(read_only=True)   #not needed in input only needed in reading
#
#     #called after validation and before saving
#     def create(self,validated_data):
#         print(validated_data)
#         e=Employee.objects.create(**validated_data)
#         e.save()
#         return e
#
#     def update(self,e,validated_data):
#         e.empid=validated_data.get('empid',e.empid)
#         e.name=validated_data.get('name',e.name)
#         e.age=validated_data.get('age',e.age)
#         e.gender = validated_data.get('gender', e.gender)
#         e.salary = validated_data.get('salary', e.salary)
#         e.designation = validated_data.get('designation', e.designation)
#         e.joining_year = validated_data.get('joining_year', e.joining_year)
#         e.save()
#         return e


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:  # used to give description about serializer class
        model=Employee
        fields='__all__'
        read_only_fields=["id","joining_year"]


    # def validate(self,data):
    #     if data['age']<=0:
    #         raise serializers.ValidationError('Age should be positive')
    #     return data
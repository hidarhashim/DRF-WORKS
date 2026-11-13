from rest_framework import serializers
from django.contrib.auth.models import User
from patient.models import Patient
from datetime import datetime
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']

    def create(self, validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"
        read_only_fields=['id','created','appointment_time','token_number']


    #validation for token and date (to limit appointment)
    def validate(self, data):
        d=data['doctor'] #doctor id from input data
        date=data['appointment_date'] #appointment date from nput data

        #find the last record matching with d and date
        a=Patient.objects.filter(doctor=d,appointment_date=date).last()
        if a:  #if last record is there
            if a.token_number==25: #check its token number is 25 if yes raises error
                raise serializers.ValidationError('Slots are full')

        today_date=datetime.today().date()
        if date<today_date:
            raise serializers.ValidationError('Invalid date')

        return data
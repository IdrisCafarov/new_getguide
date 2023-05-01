from rest_framework import serializers
from getguide_account.models import *


class BusyDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusyDates
        fields = ['id','date', 'user']



class UserBusyDate(serializers.ModelSerializer):
    dates = BusyDateSerializer(source="busy_dates",many=True)
    class Meta:
        model = MyUser
        fields = ('id','dates')

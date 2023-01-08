from rest_framework import serializers
from django.db import models
from .models import *

class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebUserSerializer
        app_label = 'quickstart'
        fields = '__all__'
from rest_framework import serializers

from .models import Application



class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['type', 'budget', 'client_name', 'client_contact', 'comment']
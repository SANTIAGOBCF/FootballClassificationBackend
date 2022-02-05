from dashboard.models import Features
from rest_framework import serializers

# Serializers define the API representation.
class FeaturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Features
        fields = '__all__' 

class FeaturesPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Features
        exclude=['position']
    
    def print_instance_attributes(self):
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)



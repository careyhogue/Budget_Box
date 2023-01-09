from .models import Category
from rest_framework import serializers

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'


    def validate(self, data):
        errors =  {}
        if 'name' not in data:
            errors['name'] = ['name is required.']

        if bool(errors):
            raise serializers.ValidationError(errors)


        return data 

           


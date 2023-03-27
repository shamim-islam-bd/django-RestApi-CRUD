from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['id', 'name', 'age', 'email', 'phone', 'address'] #include all fields
        # exclude = ['phone'] #exclude phone field

    # validate age field
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("age must be greater than 18")
        return value
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("name must be greater than 3")
        if len(value) > 10:
            raise serializers.ValidationError("name must be less than 10")
        if value.isnumeric():
            raise serializers.ValidationError("name must be string")
        special_char = "!@#$%^&*()_+{}|:<>?`~"
        for i in value:
            if i in special_char:
                raise serializers.ValidationError("Special character not allowed")
        return value
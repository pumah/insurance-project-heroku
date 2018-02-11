from rest_framework import serializers
from .models import risk_type, risk_field

class riskfldSerializer(serializers.ModelSerializer):
    class Meta:
        model = risk_field
        fields = ('field_name','field_type','field_metadata')

class riskSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    rfields = riskfldSerializer(many=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = risk_type
        fields = ('risk_type','rfields')

    def create(self, validated_data):
        rfields_data = validated_data.pop('rfields')
        risk_type = risk_type.objects.create(**validated_data)
        for rfield_data in rfields_data:
            risk_field.objects.create(risk_type=risk_type, **rfield_data)
        return risk_type



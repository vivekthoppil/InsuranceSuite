from rest_framework.serializers import ModelSerializer

from .models import Attribute, AttributeType, RiskType


class RiskTypeSearchSerializer(ModelSerializer):

    class Meta:
        model = RiskType
        exclude = ('deleted',)
        read_only_fields = ('id', 'name', 'description')


class AttributeTypeSerializer(ModelSerializer):

    class Meta:
        model = AttributeType
        fields = '__all__'
        read_only_fields = ('id', 'name', 'description',)


class AttributeSerializer(ModelSerializer):
    attribute_type = AttributeTypeSerializer(read_only=True)

    class Meta:
        model = Attribute
        fields = '__all__'
        read_only_fields = ('id', 'label', 'options', 'description',
                            'required', 'deleted')


class RiskTypeDetailSerializer(ModelSerializer):
    attributes = AttributeSerializer(read_only=True, many=True)

    class Meta:
        model = RiskType
        fields = '__all__'
        read_only_fields = ('id', 'name', 'description', 'deleted')

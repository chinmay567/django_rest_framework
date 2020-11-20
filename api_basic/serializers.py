from rest_framework import serializers
from . models import article


# class articleserializer(serializers.Serializer):
''' its a normal serializer like forms.form'''
# title = serializers.CharField(max_length=100)
# author = serializers.CharField(max_length=100)
# email = serializers.EmailField(max_length=100)
# date = serializers.DateTimeField

# def create(self, validated_date):
#     return article.objects.create(validated_date)

# def update(self, instance, validated_date):
#     instance.title = validated_date.get('title', instance.title)
#     instance.author = validated_date.get('author', instance.author)
#     instance.email = validated_date.get('email', instance.email)
#     instance.date = validated_date.get('date', instance.date)
#     instance.save()
#     return instance


class articleserializer(serializers.ModelSerializer):
    '''its a model serializer like as model form'''
    class Meta:
        model = article
        fields = ['id', 'title', 'author']


from django.conf import settings
from rest_framework import serializers
from .models import CoursesPost ,StepsPost , CategoriesPost , SectionPost ,ParcoursPost ,LevelPost





class CategoriesPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoriesPost
        fields = '__all__'
        lookup_field = 'slug'


class ParcoursPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcoursPost
        fields = '__all__'
        lookup_field = 'slug'
    def to_representation(self, instance):
        rep = super(ParcoursPostSerializer, self).to_representation(instance)
        rep['Categories'] = instance.Categories.title
        return rep

class LevelPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelPost
        fields = '__all__'
        lookup_field = 'slug'
    def to_representation(self, instance):
        rep = super(LevelPostSerializer, self).to_representation(instance)
        rep['Categories'] = instance.Categories.title
        return rep

class CoursesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesPost
        fields = '__all__'
        lookup_field = 'slug'
    def to_representation(self, instance):
        rep = super(CoursesPostSerializer, self).to_representation(instance)
        rep['level'] = instance.Categories.title
        return rep

class SectionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionPost
        fields = '__all__'
        lookup_field = 'slug'
    def to_representation(self, instance):
        rep = super(SectionPostSerializer, self).to_representation(instance)
        rep['courses'] = instance.courses.title
        return rep

class StepsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepsPost
        fields = '__all__'
        lookup_field = 'slug'

    def to_representation(self, instance):
        rep = super(StepsPostSerializer, self).to_representation(instance)
        rep['section'] = instance.section.title
        return rep
        

        
from rest_framework import serializers
from .models import Intern, Education, Training, WorkExperience

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    tel = serializers.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'tel')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', ''),
        )
        user.profile.tel = validated_data.get('tel', '')
        user.profile.save()
        return user

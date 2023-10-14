from django.test import TestCase
from django.contrib.auth import get_user_model
from app.models import User

User=get_user_model()
admin = User.objects.get(username='admin') 

admin.is_superuser = True
admin.is_staff = True 
admin.is_student = False
admin.is_teacher = False
admin.save()



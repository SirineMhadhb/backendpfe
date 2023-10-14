from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import CoursesPost ,StepsPost , CategoriesPost ,SectionPost , ParcoursPost ,LevelPost
from blog.serializers import CoursesPostSerializer ,StepsPostSerializer , CategoriesPostSerializer ,SectionPostSerializer , ParcoursPostSerializer ,LevelPostSerializer 
from django.views.decorators.csrf import csrf_exempt






    
@csrf_exempt
  
@api_view(["GET"])
def get_all_Parcours(request):
    
    parcours = ParcoursPost.objects.all().order_by('-date_created')
    serlisers = ParcoursPostSerializer(parcours , many=True)
    return Response(serlisers.data)

@api_view(["get"])
@csrf_exempt
def Level_by_slug(request , slug):
    try :
        parcours = ParcoursPost.objects.get(slug = slug)
        parcours_ser = ParcoursPostSerializer(parcours , many=False)
        level = LevelPost.objects.filter(parcours = parcours)
        level_ser = LevelPostSerializer(level , many=True)
        data = parcours_ser.data
        data["level"] = level_ser.data
        return Response(data)
    except ParcoursPost.DoesNotExist:
        return Response(f"no cours with this slug : {slug}")
@api_view(["get"])
@csrf_exempt
def Section_by_slug(request , slug):
    try :
        courses = CoursesPost.objects.get(slug = slug)
        courses_ser = CoursesPostSerializer(courses , many=False)
        section = SectionPost.objects.filter(courses = courses)
        section_ser = SectionPostSerializer(section , many=True)
        data = courses_ser.data
        data["section"] = section_ser.data
        return Response(data)
    except CoursesPost.DoesNotExist:
        return Response(f"no cours with this slug : {slug}")

@api_view(["get"])
@csrf_exempt
def Courses_by_slug(request , slug):
    try :
        level = LevelPost.objects.get(slug = slug)
        level_ser = LevelPostSerializer(level , many=False)
        courses = CoursesPost.objects.filter(level = level)
        courses_ser = CoursesPostSerializer(courses , many=True)
        data = level_ser.data
        data["courses"] = courses_ser.data
        return Response(data)
    except LevelPost.DoesNotExist:
        return Response(f"no cours with this slug : {slug}")  

@api_view(["get"])
@csrf_exempt
def Steps_by_slug(request , slug):
    try :
        section = SectionPost.objects.get(slug = slug)
        section_ser = SectionPostSerializer(section , many=False)
        steps = StepsPost.objects.filter(section = section)
        steps_ser = StepsPostSerializer(steps , many=True)
        data = section_ser.data
        data["steps"] = steps_ser.data
        
        return Response(data)
    except SectionPost.DoesNotExist:
        return Response(f"no cours with this slug : {slug}")
    


@api_view(["get"])
@csrf_exempt
def get_all_categories(request):
    categories = CategoriesPost.objects.all()
    serlisers = CategoriesPostSerializer(categories , many=True)
    return Response(serlisers.data)



class CoursesPostListView(ListAPIView):
    queryset = CoursesPost.objects.order_by('-date_created')
    serializer_class = CoursesPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


class CoursesPostDetailView(RetrieveAPIView):
    queryset = CoursesPost.objects.order_by('-date_created')
    serializer_class = CoursesPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


class CategoriesListView(ListAPIView):
    queryset = CategoriesPost.objects.all()
    serializer_class = CategoriesPostSerializer
    #lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )



class CoursesPostCategoryView(APIView):
    serializer_class = CoursesPostSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = CoursesPost.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = CoursesPostSerializer(queryset, many=True)

        return Response(serializer.data)


class StepsPostListView(ListAPIView):
    queryset = StepsPost.objects.order_by('-date_created')
    serializer_class = StepsPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class StepsPostDetailView(RetrieveAPIView):
    queryset = StepsPost.objects.order_by('-date_created')
    serializer_class = StepsPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class StepsPostCategoryView(APIView):
    serializer_class = CoursesPostSerializer
    permission_classes = (permissions.AllowAny, )
    @csrf_exempt
    def post(self, request, format=None):
        data = self.request.data
        category = data['Category']
        queryset = StepsPost.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = StepsPostSerializer(queryset, many=True)

        return Response(serializer.data)
    
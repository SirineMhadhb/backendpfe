from django.urls import path
from .views import CoursesPostListView, CoursesPostDetailView, CoursesPostCategoryView ,StepsPostListView ,StepsPostListView ,StepsPostCategoryView ,CategoriesListView, StepsPostDetailView  , Steps_by_slug , get_all_categories ,Section_by_slug ,Level_by_slug ,Courses_by_slug ,get_all_Parcours
urlpatterns = [
    path('Steps/flash/<slug>', StepsPostListView.as_view()),
    path('', CoursesPostListView.as_view()),
    path('all_Parcours', get_all_Parcours , name="list_of_Parcours"),
    path('Level/<slug>', Level_by_slug , name="list_of_Level_by_parcours"),
    path('courses/<slug>', Courses_by_slug , name="list_of_Steps_by_courses"),
    path('Steps/<slug>', Steps_by_slug , name="list_of_Steps_by_courses"),

    path('section/<slug>', Section_by_slug , name="list_of_Steps_by_steps"),
   
    path('all_categories', get_all_categories , name="list_of_all_categories"),

    #path('category', CoursesPostCategoryView.as_view()),
    path('<slug>', CoursesPostDetailView.as_view()),
    path('Steps/<slug>', StepsPostDetailView.as_view()),
    
]

from django.urls import path, include
from knox import views as knox_views
from .views import TeacherSignUpAPI, TeacherSignInAPI, TeacherMainUser, StudentSignUpAPI, StudentSignInAPI, \
    StudentMainUser, AISignUpAPI, AISignInAPI, AIMainUser

urlpatterns = [
    path('auth/', include('knox.urls')),
    path('auth/register/teacher', TeacherSignUpAPI.as_view()),
    path('auth/login/teacher', TeacherSignInAPI.as_view()),
    path('auth/user/teacher', TeacherMainUser.as_view()),

    path('auth/register/student', StudentSignUpAPI.as_view()),
    path('auth/login/student', StudentSignInAPI.as_view()),
    path('auth/user/student', StudentMainUser.as_view()),

    path('auth/register/ai', AISignUpAPI.as_view()),
    path('auth/login/ai', AISignInAPI.as_view()),
    path('auth/user/ai', AIMainUser.as_view()),

    path('auth/logout', knox_views.LogoutView.as_view(), name="knox-logout"),
]

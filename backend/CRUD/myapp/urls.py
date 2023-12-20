"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("studentapi",ClassBasedModelViewset,basename="student")
router.register("studentapi-readonly",ClassBasedModelViewsetReadOnly,"studentapi")
urlpatterns = [
    path('basicapi/', student_api_from_base),
    path('function-view-api/', student_api_api_view),
    path('generic_mixin_get/', Student_Generic_Mixin_get.as_view()),
    path('generic_mixin_post/', Student_Generic_Mixin_post.as_view()),
    path('generic_mixin_retrieve/<int:pk>/', Student_Generic_Mixin_retrive.as_view()),
    path('concrete-retrieve/<int:pk>/', Concrete_Retrive.as_view()),
    path('concrete-get-list/', Concrete_List.as_view()),
    path('concrete-post/', Concrete_Post.as_view()),
    path('concrete-update/<int:pk>/', Concrete_Update.as_view()),
    path('concrete-delete/<int:pk>/', Concrete_Destroy.as_view()),
    path("",include(router.urls))
    
]

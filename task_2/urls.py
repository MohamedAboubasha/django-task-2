from django.urls import path, include

from rest_framework.routers import DefaultRouter

from task_2 import views

router = DefaultRouter()
router.register('user', views.UserProfileViewSet)
router.register('course', views.CourseViewSet)
router.register('article', views.ArticleViewSet)
router.register('category', views.CategoryViewSet)
router.register('partner', views.PartnerViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]

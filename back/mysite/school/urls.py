from rest_framework import routers
from . views import PrensenceControlViewSet, CourseViewSet, StudentViewSet

router = routers.SimpleRouter()
router.register(r'presence', PrensenceControlViewSet)
router.register(r'course', CourseViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = router.urls


# from django.urls import path

# from . import views

# urlpatterns = [
#     # path('presence/',
#     #      views.PrensenceControlViewSet.as_view(),
#     #      name='list_create_pregnancyrisks'),
#     url(r'^api/v1/airline/(?P<pk>\d+)/$',
#         views.PrensenceControlViewSet.as_view(), name='airline_financial_data'),

# ]

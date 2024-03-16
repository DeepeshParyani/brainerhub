from rest_framework.routers import DefaultRouter
from employee.views import AddDataViewSet

router = DefaultRouter()
app_name = "employee"

router.register(r"add", AddDataViewSet, basename="add-data")

urlpatterns = []
urlpatterns += router.urls

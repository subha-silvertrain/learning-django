from django.contrib import admin
from django.urls import include, path

# Mysite is the giant root directory, and all these are directions for where the urls should go
# For example, the path polls should go to polls.urls to see further directions
# Every new path should use include("smth"), the admin one is special so its different

urlpatterns = [
    path("polls/", include("polls.urls")), 
    path("admin/", admin.site.urls),
]
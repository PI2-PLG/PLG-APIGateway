"""gateway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from users.views import NewUser, UserLogin, GetUserData, AllTokens
from endpoints.views import GetModuleList, GetAllData, GetModule, PostModuleData, ModulesToMap, AllNotifications, AllCharts, ModulesCount

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('mock.urls')),
    path('new-user/', NewUser.as_view()),
    path('get-user/', GetUserData.as_view()),
    path('login/', UserLogin.as_view()),
    path('tokens/', AllTokens.as_view()),
    path('modules-list/', GetModuleList.as_view()),
    path('all-modules-data/', GetAllData.as_view()),
    path('get-module/', GetModule.as_view()),
    path('new-module-data/', PostModuleData.as_view()),
    path('modules-map/', ModulesToMap.as_view()),
    path('all-notifications/', AllNotifications.as_view()),
    path('all-charts', AllCharts.as_view()),
    path('total-modules', ModulesCount.as_view()),
]
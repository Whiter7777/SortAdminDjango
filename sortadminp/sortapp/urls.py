from django.contrib import admin
from django.urls import path, include, re_path
from sortapp import views

urlpatterns = [
    re_path(r'login_success/$', views.login_success, name='login_success'),
    path("", views.main_auth, name = "main_auth"),
    path("main/", views.main, name = "main"),
    path("create/", views.create_analysis_record, name = "create_analysis_record"),
    path("view/", views.viewing, name = "viewing"),
    path("all/", views.viewing_all, name = "viewing_all"),
    path("view/delete_analysis/<int:id>/", views.del_analysis, name = "del_analysis"),
    path("view/delete_analysis_record/<int:id>/", views.del_analysis_record, name = "del_analysis_record"),
    path("all/delete_analysis/<int:id>/", views.del_analysis, name="del_analysis"),
    path("all/delete_analysis_record/<int:id>/", views.del_analysis_record, name="del_analysis_record"),


]


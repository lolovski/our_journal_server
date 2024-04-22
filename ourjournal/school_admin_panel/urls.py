from django.urls import path

from school_admin_panel import views

app_name = 'school_admin_panel'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_class/', views.AddClass.as_view(), name='add_class'),
    path('classes_list/', views.classes_list, name='classes_list'),
    path('classes_list/class_delete/<int:class_id>/', views.class_delete, name='class_delete'),
    path('add_students/<int:class_id>/<int:count_student>', views.add_class_students, name='add_class_students'),
    path('add_shedule/<int:class_id>/', views.add_shedule, name='add_shedule'),
    path('add_student/<int:class_id>/', views.add_student, name='add_student'),
    path('update_year', views.update_year, name='update_year'),
    path('update_shedule', views.update_shedule, name='update_shedule'),
    path('delete_shedule/<int:class_id>/', views.delete_shedule, name='delete_shedule'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mark_input/', views.mark_input, name='mark_input'),
    path('mark_input_success/', views.mark_input_success, name='mark_input_success'),
    path('signin_as_student/', views.signin_as_student, name='signin_as_student'),
    path('signin_as_teacher/', views.signin_as_teacher, name='signin_as_teacher'),
    path('register_as_student/', views.register, name='register_as_student'),
    path('register_as_teacher/', views.register, name='register_as_teacher'),
    path('view-marks/', views.view_marks, name='view_marks'),
    path('view-marks-all/', views.view_marks_all, name='view_marks_all'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('login/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout_view'),
    path('generate_report_card/', views.generate_report_card, name='generate_report_card'),
    path('enter_details/', views.upload_file, name='upload_file'),
    path('download-report/', views.view_pdf_report, name='view_report_card'),
]
"""RS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from drugs_rec import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('query_user_info', views.query_user_info, name='query_user_info'),
    
    #----------------医生功能相关映射---------------
    path('doctor_menu/<str:user_id>/', views.doctor_menu, name='doctor_menu'),
    #患者信息管理
    path('patient_info_management/', views.patient_info_management, name='patient_info_management'),
    path('add_patient_info/', views.add_patient_info, name='add_patient_info'),
    path('query_patient_info/', views.query_patient_info, name='query_patient_info'),

    #药物信息管理
    path('drug_info_management/', views.drug_info_management, name='drug_info_management'),
    path('add_drug_info/', views.add_drug_info, name='add_drug_info'),
    path('query_drug_info/', views.query_drug_info, name='query_drug_info'),

    #系统用户管理
    path('system_user_management/', views.system_user_management, name='system_user_management'),
    path('add_user_info/', views.add_user_info, name='add_user_info'),
    path('query_sysuser_info/', views.query_sysuser_info, name='query_sysuser_info'),

    #----------------患者功能相关映射---------------
    path('patient_menu/<str:user_id>/', views.patient_menu, name='patient_menu'),
    #抑郁程度评估
    path('depression_assessment/<str:user_id>/', views.depression_assessment, name='depression_assessment'),
    path('madrs_assessment_submit/<str:user_id>/', views.madrs_assessment_submit, name='madrs_assessment_submit'),
    
    #焦虑程度评估
    path('anxiety_assessment/<str:user_id>/', views.anxiety_assessment, name='anxiety_assessment'),
    path('hars_assessment_submit/<str:user_id>/', views.hars_assessment_submit_view, name='hars_assessment_submit'),
    
    #个人信息管理
    path('personal_info_management/<str:user_id>/', views.personal_info_management, name='personal_info_management'),
    
    #获取药物诊疗推荐信息
    path('get_medication_advice/<str:user_id>/', views.get_medication_advice, name='get_medication_advice'),
    path('drug_list', views.drug_list, name='drug_list'),



]

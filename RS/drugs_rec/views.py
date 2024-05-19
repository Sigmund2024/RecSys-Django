from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv  # Assuming CSV format for data files

def welcome(request):
    return render(request, 'welcome.html')

def query_user_info(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id.startswith('P'):
            # 如果用户ID以'P'开头，返回患者菜单界面
            user_id=user_id.replace('P','')
            return redirect('patient_menu', user_id=user_id)
        elif user_id.startswith('D'):
            # 如果用户ID以'D'开头，跳转到医生菜单界面
            return redirect('doctor_menu', user_id=user_id)
        else:
            return HttpResponse('Invalid input format. Please enter a valid user ID.')
    else:
        return HttpResponse('Invalid request.')
#------------------------------------医生相关的功能---------------------------------------
def doctor_menu(request, user_id):
    # 处理医生菜单页面的逻辑
    return render(request, 'doctor_menu.html', {'user_id': user_id})

#-----------------患者信息管理-------------------
def patient_info_management(request):
    return render(request, 'patient_info_management.html')

def add_patient_info(request):
    if request.method == 'POST':
        add_name = request.POST.get('add_name')
        add_gender = request.POST.get('add_gender')
        add_age = request.POST.get('add_age')
        add_email = request.POST.get('add_email')
        # 进行添加患者信息的逻辑处理
        return HttpResponse('Patient Information Added Successfully.')
    else:
        return HttpResponse('Invalid request.')

def query_patient_info(request):
    if request.method == 'POST':
        query_patient_id = request.POST.get('query_patient_id')
        # 进行查询患者信息的逻辑处理
        return HttpResponse('Query Result for Patient ID {}: ...'.format(query_patient_id))
    else:
        return HttpResponse('Invalid request.')
    
#-----------------药物信息管理-------------------
def drug_info_management(request):
    # 处理药物信息管理逻辑
    return render(request, 'drug_info_management.html')

def add_drug_info(request):
    if request.method == 'POST':
        add_drug_id = request.POST.get('add_drug_id')
        add_drug_name = request.POST.get('add_drug_name')
        add_drug_type = request.POST.get('add_drug_type')
        # 进行新增药物信息的逻辑处理
        return HttpResponse('Drug Information Added Successfully.')
    else:
        return HttpResponse('Invalid request.')
    
def query_drug_info(request):
    if request.method == 'POST':
        query_drug_id = request.POST.get('query_drug_id')
        # 进行查询药物信息的逻辑处理
        return HttpResponse('Query Result for Drug ID {}: ...'.format(query_drug_id))
    else:
        return HttpResponse('Invalid request.')

#-----------------系统用户管理-------------------
def system_user_management(request):
    return render(request, 'system_user_management.html')

def add_user_info(request):
    if request.method == 'POST':
        add_user_id = request.POST.get('add_user_id')
        add_user_password = request.POST.get('add_user_password')
        add_user_role = request.POST.get('add_user_role')
        # 进行新增用户信息的逻辑处理，包括密码
        return HttpResponse('User Information Added Successfully.')
    else:
        return HttpResponse('Invalid request.')

def query_sysuser_info(request):
    if request.method == 'POST':
        query_user_id = request.POST.get('query_sysuser_id')
        # 进行查询用户信息的逻辑处理
        return HttpResponse('Query Result for User ID {}: ...'.format(query_user_id))
    else:
        return HttpResponse('Invalid request.')

#------------------------------------患者相关的功能---------------------------------------
def patient_menu(request,user_id):
    return render(request, 'patient_menu.html', {'user_id': user_id})

def depression_assessment(request,user_id):
    return render(request, 'depression_assessment.html', {'user_id': user_id})

def madrs_assessment_submit(request,user_id):
    if request.method == 'POST':
        # 处理提交的表单数据
        question1 = request.POST.get('question1')
        # 处理更多问题的数据

        # 在这里处理评估逻辑，例如计算得分等
        # 返回评估结果或者跳转到结果页面
    else:
        return HttpResponse('Invalid request.')  # 处理非 POST 请求的情况

#焦虑程度评估
def anxiety_assessment(request,user_id):
    return render(request, 'anxiety_assessment.html', {'user_id': user_id})

def hars_assessment_submit_view(request,user_id):
    if request.method == 'POST':
        # 处理表单提交逻辑
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')  
        question4 = request.POST.get('question4')
        
        # 这里可以根据表单提交的内容进行相应的处理，比如计算得分等
        
        return HttpResponse('Assessment submitted successfully.')
    else:
        return HttpResponse('Invalid request method.')

#个人信息管理
def personal_info_management(request,user_id):
    user_data = read_user_data()
    user = find_user_by_id(user_data, user_id)
    if user:
        return render(request, 'confirm_user_info.html', {'user': user})
    else:
        return HttpResponse('User ID not found.')
    

#获取药物诊疗推荐信息
def get_medication_advice(request,user_id):
    return render(request, 'get_medication_advice.html', {'user_id': user_id})

def drug_list(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        k=int(request.POST.get('k_value'))
        try:
            # Placeholder for recommendation module
            recommended_drugs = recommend_drugs(user_id,k)
            if not recommended_drugs:
                return HttpResponse('No recommendations found for user ID: {}'.format(user_id))
            return render(request, 'drug_list.html', {'recommended_drugs': recommended_drugs,'k' : k})
        except Exception as e:
            return HttpResponse('Error: {}'.format(str(e)))
    else:
        return HttpResponse('Invalid request.')

#------------------------------------数据处理---------------------------------------

def read_user_data():
    # Code to read user data from file
    user_data = []
    with open('data/user_data.dat', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            sex = 'Male' if row[2] == 1 else 'Female'
            user_data.append({
                'id': row[0],
                'age': row[1],
                'sex': sex,
                'madrs_score': row[3],
                'ham_a_score': row[4]
            })
    return user_data


def read_item_data():
    # Code to read user data from file
    item_data = {}
    with open('data/drug_data.txt', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            item_data[row[1]]=row[0]
            #print(row[1],item_data[row[1]])
    return item_data

def find_user_by_id(user_data, user_id):
    # Code to find user by ID in user data
    for user in user_data:
        if user['id'] == user_id:
            return user
    return None

def get_user_interest(user_id, k):
    file_path = 'data/sorted_rec_result.txt'
    if k>50 :
        k=50
    with open(file_path, 'r') as file:
        for line in file:
            user_info = line.split('::')
            #print(user_info[0],eval(user_info[1]))
            if user_info[0] == str(user_id):
                print(user_info[0],eval(user_info[1]))
                item_ids = eval(user_info[1])  # Convert string representation of list to actual list
                #print(item_ids[:k])
                return item_ids[:k]  # Return top k item IDs
    return []  # Return empty list if user ID is not found in the file

def recommend_drugs(user_id,k):
    item_data=read_item_data()
    #直接读取用户最感兴趣的k个药物
    item_ids = get_user_interest(user_id, k)
    print(item_ids)
    #如果没有找到用户的兴趣药物，返回空列表
    if not item_ids:
        return []
    
    #recommended_drugs中包含多个字典，每个字典包含药物的id和name
    recommended_drugs = []
    for id in item_ids:
        print(id,item_data[str(id)])
        recommended_drugs.append({
            'id': id,
            'name': item_data[str(id)]
        })
    return recommended_drugs
    


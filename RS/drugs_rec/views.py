from django.shortcuts import render
from django.http import HttpResponse
from .models import SumAggregator
import csv  # Assuming CSV format for data files
from tensorflow.keras.models import load_model
import tensorflow as tf


def welcome(request):
    return render(request, 'welcome.html')

def query_user_info(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user_data = read_user_data()
            user = find_user_by_id(user_data, user_id)
            if user:
                return render(request, 'confirm_user_info.html', {'user': user})
            else:
                return HttpResponse('User ID not found.')
        except Exception as e:
            return HttpResponse('Error: {}'.format(str(e)))
    else:
        return HttpResponse('Invalid request.')

def drug_list(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        k=int(request.POST.get('k'))
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
    


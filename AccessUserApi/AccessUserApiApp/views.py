from django.shortcuts import render, HttpResponse, redirect
import requests, json

# Create your views here.
def home(request):
    data = request.GET.get('data', '')
    return render(request,'home.html', {'data': data})
def viewAllData(request):
    URL = "https://userapi.rainbowitpoint.com/user-info/"

    response = requests.get(url=URL)
    #-----extract into json
    data_list = response.json()
    context = {
        'data_list': data_list,
    }
    return render(request,'viewdata.html',context)

def viewSingleData(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        URL = f"https://userapi.rainbowitpoint.com/user-info/{id}"
        response = requests.get(url=URL)
        #-----extract into json
        if(response):
            print('if work')
            data = response.json()
            context = {
                'data': data,
            }
            return render(request,'viewsingledata.html',context)
        else:
            print('else work')
            context = {
                'error': 'Data not found',
            }
            return render(request,'viewsingledata.html',context)

def deleteData(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        
        URL = f"https://userapi.rainbowitpoint.com/user-delete/"
        
        data = {
            'id': id
        }

        json_data = json.dumps(data)
        r = requests.delete(url=URL, data = json_data)
        #-----extract into json
        data = r.json()
        return redirect('home')

def insertData(request):
    URL = "https://userapi.rainbowitpoint.com/user-create/"
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        website = request.POST.get('website')
        
        data = {
            "name":name,
            "username":username,
            "email":email,
            "address":address,
            "website":website,
        }
        
        json_data = json.dumps(data)
        re = requests.post(url=URL, data = json_data)
        data = re.json()
        return redirect('viewAllData')
    
    return render(request,'insertdata.html')
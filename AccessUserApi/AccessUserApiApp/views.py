from django.shortcuts import render, HttpResponse, redirect
import requests, json

# Create your views here.
def home(request):
    
    return render(request,'home.html')
def viewAllData(request):
    URL = "https://userapi.rainbowitpoint.com/user-info/"

    response = requests.get(url=URL)
    #-----extract into json
    data_list = response.json()
    context = {
        'data_list': data_list,
    }
    return render(request,'viewdata.html',context)

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
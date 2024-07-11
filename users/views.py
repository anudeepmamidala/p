from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel
from django.core.files.storage import FileSystemStorage

# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})
def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})
def UserHome(request):
    return render(request, 'users/UserHome.html', {})


def cifarTraining(request):
    from .utility.cifar10_training_model import start_cifar_training
    # result = start_cifar_training()
    return render(request, 'users/cifarTraining.html',{})

def cifarvggtraining(request):
    from .utility.vgg16model import startvgg16
    # result = startvgg16()
    return render(request, 'users/cifarvgg16model.html', {})

def cifarresnettraining(request):
    from .utility.resnettraining import start_resnet
    result = start_resnet()
    return render(request, 'users/cifarresnetmodel.html', {})

def userTestPrediction(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        from .utility import test_predections
        result = test_predections.start_test(filename)
        print('Result:', result)
        return render(request, "users/testform.html", {"result": result, "path": uploaded_file_url})
    else:
        return render(request, "users/testform.html", {})
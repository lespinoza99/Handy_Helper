from django.shortcuts import render, redirect
from .models import User, Job
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    print(User.objects.all())
    return render(request, 'index.html')


def new_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')

    fname = request.POST['first_name']
    lname = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    print('#'*40)
    print("unhashed", password)
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print("hashed", pw_hash)

    UserX = User.objects.create(
        first_name=fname, last_name=lname, email=email, password=pw_hash)
    user_test = UserX.id
    request.session['user_logged'] = user_test
    print('THIS IS THE USER ID!', user_test)

    return redirect('/success')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')
    list_of_users = User.objects.filter(email = request.POST['email'])
    if len(list_of_users) > 0:
        user = list_of_users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_logged'] = user.id
            return redirect('/success')
    
    return redirect('/')



def success(request):
    UserX_id = request.session['user_logged']
    x = User.objects.get(id=UserX_id)

    all_jobs = Job.objects.all()

    
    context = {

        'User_logged_in': x,
        'all_jobs': all_jobs,
        

    }
    return render(request, 'success.html', context)

def new_job(request):
    user_logged = request.session['user_logged']

    logged = User.objects.get(id = user_logged)
    context = {
        'user_logged': logged,
    }
    return render(request, 'new_job.html', context)

def create_job(request):
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/jobs/new')
    
    Title = request.POST['title']
    Location = request.POST['location']
    Description = request.POST['desc']
    userid = User.objects.get(id =request.POST['UserID'])
    Job.objects.create(title = Title, location = Location, description = Description, user = userid )
    
    return redirect('/success')

def job_desc(request, job_id):
    UserX_id = request.session['user_logged']
    x = User.objects.get(id=UserX_id)

    job = Job.objects.get(id= job_id)
    
    context = {
        'user_logged' : x,
        'job' :job,

    }
    return render(request, 'job_info.html', context)

def job_edit(request, job_id):
    UserX_id = request.session['user_logged']
    x = User.objects.get(id=UserX_id)
    job = Job.objects.get(id = job_id)

    context = {
        'user_logged' : x,
        'job': job
    }
    return render(request, 'job_edit.html', context)

def complete_edit(request, job_id):
    jobID = job_id
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect(f'/jobs/edit/{jobID}')

    job = Job.objects.get(id = job_id)
    job.title = request.POST['title']
    job.description = request.POST['desc']
    job.location = request.POST['location']
    job.save()
    return redirect('/success')

def edit_function(request, book_id, user_id):
    this_job = Job.objects.get(id = book_id)
    this_user = User.objects.get(id = user_id)
    pass


def deletejob(request, jobid):
    bob = Job.objects.get(id = jobid)
    bob.delete()
    return redirect('/success')


def destroy(request):
    del request.session['user_logged']
    return redirect('/')



from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    test = "Working!!"
    current_user = request.user
    profile = MyUser.get_user()
    posts = Post.get_post()
    return render(request,'index.html',{"test":test,
                                        "current_user":current_user,
                                        "profile":profile,
                                        "posts":posts})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    test = "Working!!"
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = current_user
            new.save()
            return redirect(view_profile)
    else:
        form = CreateProfileForm()
    return render(request,'profile/create.html',{"test":test,"upload_form":form})

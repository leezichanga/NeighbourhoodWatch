from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import MyUser,Neighborhood,Post,Business
from .forms import CreateProfileForm,PostForm

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
    return render(request,'create_profile.html',{"test":test,"upload_form":form})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    myuser = MyUser.get_user()
    for user in myuser:
        if user.user.id == current_user.id:
            if request.method == 'POST':
                post_form = PostForm(request.POST,request.FILES)
                if post_form.is_valid():
                    post = post_form.save(commit=False)
                    post.editor = user
                    post.save()
                    return redirect(index)
            else:
                post_form = PostForm()
            return render(request,'write_posts.html',{"post_form":post_form})

@login_required(login_url='/accounts/login/')
def view_business(request):
    current_user = request.user
    biz = Business.get_business()
    return render(request,'business.html',{"current_user":current_user,
                                           "business":biz})
@login_required(login_url='/accounts/login/')
def view_profile(request):
    test="Working!!"
    current_user = request.user
    profile = MyUser.get_user()
    posts = Post.get_post()
    return render(request,'profile.html',{"test":test,
                                                  "profile":profile,
                                                  "current_user":current_user,
                                                  "posts":posts})

@login_required(login_url='/accounts/login/')
def view_hood(request):
    test="Neighborhood!!"
    current_user = request.user
    myuser = MyUser.get_user()
    posts = Post.get_post()
    neibahood = Neighborhood.get_neighborhood()
    return render(request,'neighborhood.html',{"test":test,
                                                   "hood":neibahood,
                                                   "posts":posts,
                                                   "myuser":myuser,
                                                   "current_user":current_user})


@login_required(login_url='/accounts/login/')
def neighborhood(request):
    test="Neighborhood!!"
    current_user = request.user
    myuser = MyUser.get_user()
    posts = Post.get_post()
    count = 0
    neibahood = Neighborhood.get_neighborhood()
    hood = get_object_or_404(Neighborhood)
    for neiba in neibahood:
        for user in myuser:
            if user.neighborhood.id == neiba.id:
                count += 1
    hood.occupants_count = count
    hood.save()
    return redirect('view_neighborhood')

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'biz' in request.GET and request.GET["biz"]:
        search_term = request.GET.get("biz")
        searched_biz = Business.find_business(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"biz":searched_biz})

    else:
        message = 'You havent searched for any term'
        return render(request,'search.html',{"message",message})

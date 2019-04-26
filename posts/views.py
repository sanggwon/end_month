from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, "posts/list.html",{"posts":posts})

def create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect("posts:list")
    else :
        post_form = PostForm()
    return render(request,"posts/create.html",{"post_form":post_form})
            
def like(request,id):
    post = Post.objects.get(id=id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else :
        post.likes.add(user)
    
    return redirect('posts:list')

        
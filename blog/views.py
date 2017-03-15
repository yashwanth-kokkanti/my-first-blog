from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from . models import Post, Comment
from . forms import PostForm, CommentForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    users = User.objects.all()
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {'posts':posts, 'users':users})
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {'post':post})
	
@login_required
def post_new(request):
    print ("request = ", request)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print ("Request inside Form is valid")
            post = form.save(commit=False)
            post.author = request.user
            #post.image = request.FILES['image']
            post.text = form.cleaned_data['text']
            post.title = form.cleaned_data['title']			
            #post.published_date = timezone.now()
            print ("Method coming here")		
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :
        print ("Request inside Form is Not valid- Else")
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

@login_required	
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.image = request.FILES['image']
            #post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk = post.pk)
    else :
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {"form":form})
	
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required	
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("post_detail", pk=pk)

@login_required
def post_remove (request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post_list")

@login_required	
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=post.pk)
    else :
        form = CommentForm()
    return render(request, "blog/add_comment_to_post.html", {'form':form} )
	
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect("post_detail", pk = comment.post.pk)
	
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("post_detail", pk=post_pk)
	
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            lusername = form.cleaned_data['username']
            lemail = form.cleaned_data['email']
            lpassword1 = form.cleaned_data['password1']
            lpassword2 = form.cleaned_data['password2']			
            if lpassword1 == lpassword2:
                password = lpassword1
            user = User.objects.create_user(username=lusername, email=lemail)
            user.set_password(password)
            user.save()
            return redirect("post_list")
    else :
        form = RegistrationForm()
    return render(request, "registration/register.html", {'form':form})
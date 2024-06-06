from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(req):
    posts = PostModel.objects.all()
    if req.method=='POST':
        form = PostModelForm(req.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = req.user
            instance.save()
            return redirect('bIndex')
    else:
        form = PostModelForm()
    context = {
        'posts':posts,
        'form':form
    }
    return render(req, 'blog/index.html',context)

@login_required
def postDetail(req, pk):
    post = PostModel.objects.get(id=pk)
    if req.method=='POST':
        cForm = CommentForm(req.POST)
        if cForm.is_valid():
            instance = cForm.save(commit=False)
            instance.user = req.user
            instance.post = post
            instance.save()
            return redirect('postDetail', pk=post.id)
    else:
        cForm = CommentForm()
    context= {
        'post':post,
        'cForm':cForm,
    }
    return render(req, 'blog/postDetail.html', context)

@login_required
def postEdit(req, pk):
    post = PostModel.objects.get(id=pk)
    if req.method=='POST':
        form = PostUpdateForm(req.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('postDetail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context= {
        'post':post,
        'form':form,
    }
    return render(req, 'blog/postEdit.html', context)

@login_required
def postDelete(req, pk):
    post = PostModel.objects.get(id=pk)
    if req.method=='POST':
        post.delete()
        return redirect('bIndex')
    context= {
        'post':post,
    }
    return render(req, 'blog/postDelete.html', context)
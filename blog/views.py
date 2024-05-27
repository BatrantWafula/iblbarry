# views.py
from django.shortcuts import render, redirect
from .models import Post, Subscriber
from .forms import PostForm, SubscriberForm

def index(request):
    posts = Post.objects.all()
    subscribers = Subscriber.objects.all()
    default_image_url = "https://images.pexels.com/photos/1519088/pexels-photo-1519088.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"

    if request.method == 'POST':
        if 'submit_post' in request.POST:
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post_form.save()
                return redirect('success')
        else:
            post_form = PostForm()

        if 'submit_subscriber' in request.POST:
            subscriber_form = SubscriberForm(request.POST)
            if subscriber_form.is_valid():
                subscriber_form.save()
                return redirect('success')
        else:
            subscriber_form = SubscriberForm()
    else:
        post_form = PostForm()
        subscriber_form = SubscriberForm()

    context = {
        'posts': posts,
        'subscribers': subscribers,
        'default_image_url': default_image_url,
        'post_form': post_form,
        'subscriber_form': subscriber_form,
    }

    return render(request, 'index.html', context)

def success_view(request):
    return render(request, 'success.html')

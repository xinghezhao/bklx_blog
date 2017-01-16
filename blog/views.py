#coding:utf-8
from django.shortcuts import render

from blog.models import Catagory,Tag,Blog,Comment,Achievement,Person,Speak,Skill,Life,Aboutme
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse

from blog.forms import CommentForm



def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')

    #对首页进行分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(blogs, 5, request=request)

    all_blogs = p.page(page)


    all_timeline = Speak.objects.all().order_by('-created')

    first_timeline = all_timeline[:1]

    return render(request, 'blog-list.html', {
        'blogs':all_blogs,
        'first_timeline':first_timeline
    })


def blogs_detail(request,blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
            
    return render(request,'blog_detail.html', {
    		'form':form,'blog':blog,'comments': blog.comment_set.all().order_by('-created')}
        )
 

def blogs_person(request):

    blogs_person = Person.objects.all()

    all_timeline = Speak.objects.all().order_by('-created')

    first_timeline = all_timeline[:1]


    return render(request,'blog_person.html',{
        'blogs_person':blogs_person,
        'first_timeline':first_timeline
    })



def person_detail(request,person_id):
    all_person= Person.objects.get(id = person_id)

    achievements = all_person.achievements.all()

    return render(request, 'blog_person_details.html', {
        'all_person':all_person,'achievements': achievements})


def timeline(request):
    
    all_timeline = Speak.objects.all().order_by('-created')


    first_timeline = all_timeline[:1]


    return render(request,'blog_timeline.html', {
        'all_timeline':all_timeline,
        'first_timeline':first_timeline
    })



def aboutme(request):

    all_aboutmes = Aboutme.objects.all()

    all_timeline = Speak.objects.all().order_by('-created')

    first_timeline = all_timeline[:1]


    return render(request,'blog_aboutme.html', {
        'all_aboutmes':all_aboutmes,
        'first_timeline':first_timeline

    })


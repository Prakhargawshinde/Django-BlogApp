from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Blog_App.forms import Blog_signup,Post_blog
from Blog_App.models import Post_blog_form
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def Blog_Welcome(request):
    return render(request,'Blog_App/Blog_Welcome.html')
@login_required
def Welcome(request):
    return render(request,'Blog_App/Welcome.html')
def Signup(request):
    Signup = Blog_signup();
    sign_dict={'Signup':Signup}
    if request.method=='POST':
        Signup = Blog_signup(request.POST)
        if Signup.is_valid():
            user=Signup.save()
            user.set_password(user.password)
            user.save()
            subject='Blog App Welcome Mail'
            message="Welcome"+user.first_name+", You are Successfully Registered"
            recipient=[user.email]
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient)
            print('Data inserted')
            sign_dict.update({'msg':'Registered Successfully'})
    return render(request,'Blog_App/Signup.html',context=sign_dict)
@login_required
def Post_blog_frm(request):
    Post_blog_frm = Post_blog()
    post_dict={'Post_blog':Post_blog_frm}
    if request.method=='POST':
        Post_blog_frm = Post_blog(request.POST,request.FILES)
        if Post_blog_frm.is_valid():
            data = Post_blog_frm.save(commit=False)
            data.Author=request.user
            data.save()
            post_dict.update({'msg':'Blog Post Successfully'})
    return render(request,'Blog_App/Post_Blog.html',context=post_dict)

def ViewPostBlog(request):
    blog_list=Post_blog_form.objects.all().order_by('-Date_time')
    print(blog_list)
    blog_dict={'Blog':blog_list}
    return render(request,'Blog_App/View_Post_Blog.html',context=blog_dict)


def DetailView(request,id):
    blog_list=Post_blog_form.objects.get(id=id)
    blog_dict={'Blog':blog_list}
    if request.method=='POST':
        blog_list.delete()
        blog_dict.update({'msg':'Blog Deleted Successfully'})
    return render(request,'Blog_App/Detail_View.html',context=blog_dict)

from django.shortcuts import render
from Library.models import student
from Library.models import book
from Library.models import borrowing
from Library.models import Course
from Library.models import mentor
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        'firstname':'Aishah',
        'greeting':1,
    }
    return render (request, 'homepage.html',context)

def view(request):
    context = {
        'lastname': 'borrow',
    }
    return render (request, 'view.html',context)

def dbstudent(request):
        studata = student.objects.all().values()
        context = {
            "studata": studata,
        }
        return render(request,'dbstudent.html',context)

def dbbook(request):
     book1 = book.objects.all().values()
     context = {
          "book1": book1,
     }
     return render(request,'dbbook.html',context)

def dbborrow(request):
     borrow1 = borrowing.objects.all().values()
     context = {
          "borrow1": borrow1,
     }
     return render(request,'dbborrow.html',context)

def dbcourse(request):
     mycourse = Course.objects.all().values()
     dict={
          'mycourse':mycourse,
     }
     if request.method =='POST':
          c_code= request.POST['code']
          c_desc = request.POST['desc']
          data = Course(code = c_code,description=c_desc)
          data.save()
     return render(request, 'dbcourse.html',dict)

def dbmentor(request):
     mymentor = mentor.objects.all().values()
     dict = {
          'mymentor':mymentor,
     }
     if request.method == 'POST':
          c_mentor_id = request.POST['mentor_id']
          c_mentor_name = request.POST['mentor_name']
          c_mentor_room_no = request.POST['mentor_room_no']
          a = mentor(mentor_id=c_mentor_id, mentor_name = c_mentor_name, mentor_room_no = c_mentor_room_no)
          a.save()
          dict = {
               'message': 'Data is Save',
               'mymentor': mymentor
          }
     else:
          dict = {
               'message':''
          }

     return render(request,"dbmentor.html",dict)

def update_course(request,code):
     data = Course.objects.get(code=code)
     dict = {
          'data': data
     }
     return render (request, "update_course.html",dict)

def save_update_course(request,code):
     c_desc = request.POST['desc']
     data = Course.objects.get(code=code)
     data.desc = c_desc
     data.save()
     return HttpResponseRedirect(reverse("dbcourse.html"))
     

def delete_course(request, code):
     data = Course.objects.get(code=code)
     data.delete()
     return HttpResponseRedirect(reverse('dbcourse.html'))

def search_course(request):
     if request.method=='GET':
          c_code = request.GET.get("c_code")

          if c_code:
               data = Course.objects.filter(code=c_code.upper())
          else:
               data = None
          context = {
               'data':data
          }
          return render(request,"search_course.html",context)
     return render(request, "homepage.html")
          

     
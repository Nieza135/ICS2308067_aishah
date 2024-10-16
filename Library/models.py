from django.db import models

# Create your models here.
class book(models.Model):
    book_id = models.CharField(max_length=3, primary_key=True)
    title = models.CharField(max_length=50)
    author = models.EmailField()
    published_year = models.CharField(max_length = 255, null=True)

class student(models.Model):
    student_id = models.CharField(max_length=12, primary_key=True)
    studentname = models.CharField(max_length = 100)
    studentphone = models.CharField(max_length = 150)
    studentemail = models.EmailField()
    stud_status = models.CharField(max_length=10, default='Active')

class borrowing(models.Model):
    borrow_id = models.CharField(max_length=3,primary_key=True)
    book_id = models.ForeignKey(book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    borrow_date = models.DateField(max_length=10)
    retunr_date = models.DateField(max_length=10)

class Course(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    description = models.TextField()

class mentor(models.Model):
    mentor_id=models.CharField(max_length=10, primary_key=True)
    mentor_name = models.CharField(max_length=200)
    mentor_room_no = models.CharField(max_length=10, default='sk2')
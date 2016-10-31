from django.shortcuts import render
from tapp.models import MyUser, Student, Faculty

def users(request):
    #return HttpResponse("Hello, world!")
    users = MyUser.objects.all()
    
    return render(request, 'tapp/list_users.html',
                  {'users': users})

def students(request):
    # All students
    all_students = Student.objects.all().count()
    # All students on the faculty 'f1'
    f1 = Faculty.objects.get(id=1)
    students_f1 = Student.objects.filter(faculty=f1).count()
    
    # Counting all students for each faculty
    all_students_f = []
    all_faculties = Faculty.objects.all()
    for f in all_faculties:
        count = Student.objects.filter(faculty=f).count()
        all_students_f.append({"title": f.title, "count": count})
    # list of dict all students
    list_students = []
    students = Student.objects.all()
    for student in students:
        list_students.append({
            'first_name': student.first_name,
            'last_name': student.last_name,
            'faculty': student.faculty.title})
    
    return render(request, 'tapp/list_students.html',
                  {'all_students': all_students,
                   'f1': f1.title,
                   'students_f1': students_f1,
                   'all_students_f': all_students_f,
                   'list_students': list_students})
    
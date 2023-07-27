from django.shortcuts import render , HttpResponse
from .models import Student
from django.contrib import messages



# Create your views here
def index(request):
    students = Student.objects.all()
    query = request.GET.get('q')  # Get the search query from the URL parameter 'q'
    #sort_by = request.GET.get('sort_by')  # Get the sort field from the URL parameter 'sort_by'
    #sort_direction = request.GET.get('sort_direction')


    if query:
        students = students.filter(name__icontains=query)
    
    #if sort_by:
    #   if sort_direction == 'asc':
    #        students = students.order_by(sort_by)
    #   else:
    #        students = students.order_by(f'{sort_by}')


    
    
    if request.method =="POST" :
        if "add" in request.POST:
          name=request.POST.get("name")
          email=request.POST.get("email")
          mobile=request.POST.get("mobile")
          rollno=request.POST.get("rollno")
          Student.objects.create(
              name=name,
              email=email,
              mobile=mobile,
              rollno=rollno
          )
          messages.success(request, "student added successfully")
        elif "update" in request.POST:
            id=request.POST.get("id")
            name=request.POST.get("name")
            email=request.POST.get("email")
            mobile=request.POST.get("mobile")
            rollno=request.POST.get("rollno")
            
            update_student = Student.objects.get(id=id)
            update_student.name = name
            update_student.email = email
            update_student.mobile = mobile
            update_student.rollno = rollno
            
            update_student.save()
            messages.success(request, "Student's Information Updated successfully")
            
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()
            
            messages.success(request, "Student Deleted successfully")
            
        
    context={"students" : students, }#'sort_by': sort_by,'sort_direction': sort_direction,
    return render(request, 'index.html', context = context)

    
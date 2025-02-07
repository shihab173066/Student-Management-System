from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create Student
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# View Student Details
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

# Update Student
def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student details updated!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# Delete Student
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, 'Student deleted successfully!')
    return redirect('student_list')
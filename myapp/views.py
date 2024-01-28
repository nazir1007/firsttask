from django.shortcuts import render

def task_view(request):
    first_name = "Mohd"
    last_name = "Nazir"
    return render(request, "task.html", {'first_name': first_name, 'last_name': last_name})
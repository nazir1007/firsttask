from django.shortcuts import render

def task_view(request):
   context = {
       "first_name": "Mohd",
       "last_name": "Nazir",
    }
   return render(request, "task.html", context)
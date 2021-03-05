from django.shortcuts import render

# Create your views here.
# Views are always expected to return HttpResponse or an exception
posts = [
         {
          'author':'Amey Bhilegaonkar',
          'title':'Amey\'s First Blog',
          'content':'Follow me on instagram @ameygoes',
          'date_posted':'Aug-2020'
         },
         {
          'author':'Aditya Bhilegaonkar',
          'title':'Aditya\'s First Blog',
          'content':'Follow me on instagram @ameygoes',
          'date_posted':'Sep-2020'
         }
]


def home(request):
    context = {
               'posts':posts
    }
    return render(request, 'python_E2E_Django_App/home.html',context)

def about(request):
    return render(request, 'python_E2E_Django_App/about.html',{'title':'AmeyGoes'})

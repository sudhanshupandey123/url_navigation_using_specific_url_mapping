from django.shortcuts import render

# Create your views here.
def app1_htmlpage(request):
    return render(request,'app1_htmlpage.html')


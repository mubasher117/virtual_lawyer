from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'virtual_lawyer/index.html')

def about(request):
    return render(request,'virtual_lawyer/about.html')

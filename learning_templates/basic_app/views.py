from django.shortcuts import render

# Create your views here.
def index(request):
    mydict = {'text':'hello world', 'number':100}
    return render(request, 'basic_app/index.html', mydict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative_url_template(request):
    return render(request, 'basic_app/relative_url_template.html')

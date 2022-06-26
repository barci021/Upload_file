from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView



class Home(TemplateView):
    template_name = 'home.html'


def upload_arq(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)
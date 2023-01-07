from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from sunhacksapp.main import main
# Create your views here.
def index(request):
    if request.method == "GET":
        # content = {'Prescriptions': ['PARACETAMOL'], 'Diseases': ['Fever', ' Pain'], 'Ayurvedic': 'No data found'}
        return render(request, "index.html")
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage(location='sample_images/')
        filename = fs.save(myfile.name, myfile)
        location = request.POST.get('location')
        language = request.POST.get('language')
        content = main(filename, location, language)
        # print(output)
        # content = {'Prescriptions': ['PARACETAMOL'], 'Diseases': ['Fever', ' Pain'], 'Ayurvedic': 'No data found'}
        return render(request,'index.html', content)


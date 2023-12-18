from io import StringIO

from django.shortcuts import redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm, DataEntryForm
import pandas as pd
from .helpers import group_people_by_address
from .models import Person

def index(request):
    result = group_people_by_address(Person.objects.all())
    return render(request, 'index.html',  {'result': result})


def file_upload(request):
    result = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = pd.read_csv(request.FILES['csv_file'], encoding="utf-8-sig")
            records = file.to_dict(orient="records")
            for entry in records:
                try:
                    Person.objects.create(name=entry['Name'], address = entry['Address'])
                except Exception as E:
                    print(f'Found Duplocate Reocred : {str(entry['Name'])} - {str(entry['Address'])}')
                    pass

            
            result = group_people_by_address(Person.objects.all())
            return render(request, 'upload.html', {'form': form, 'result': result})
    else:
        result = group_people_by_address(Person.objects.all())
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form, 'result': result})



def data_entry(request):
    result = None
    if request.method == 'POST':
       form = DataEntryForm(request.POST)
       if form.is_valid():
        try:
            Person.objects.create(name=request.POST['name'], address = request.POST['address'])
        except Exception as E:
            print(f'Found Duplocate Reocred : {str(request.POST['name'])} - {str(request.POST['address'])}')
            pass
        
        result = group_people_by_address(Person.objects.all())

    else:
        result = group_people_by_address(Person.objects.all())
        form = DataEntryForm()

    return render(request, 'data_entry.html', {'form': form, 'result': result})


def file_download(request):
     file_obj = StringIO()
     all_names =  group_people_by_address(Person.objects.all())
     
     for inner_list in all_names:
        line = ", ".join(inner_list) + "\n"
        file_obj.write(line)
    
     file_obj.seek(0)
     response = HttpResponse(file_obj, content_type='application/text charset=utf-8')
     response['Content-Disposition'] = 'attachment; filename="result.txt"'
   
     return response


def reset_data(request):
    Person.objects.all().delete()
    return redirect(index)
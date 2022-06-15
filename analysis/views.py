from django.shortcuts import render
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Sale
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def Import_csv(request):
    print('s')
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file)
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            empexceldata['DocDate'] = pd.to_datetime(empexceldata['DocDate'])
            empexceldata.fillna(method='ffill',inplace=True)
            
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                obj = Sale.objects.create(DocDate=dbframe.DocDate,DocNo=dbframe.DocNo,Customer=dbframe.Customer,
                ProductCode = dbframe.ProductCode,ProductName=dbframe.ProductName,SalesUnit=dbframe.SalesUnit,SalesQty=dbframe.SalesQty)

                print(type(obj))
                obj.save()
            return render(request, 'analysis/importexcel.html',{'uploaded_file_url': uploaded_file_url})
    except Exception as identifier:
        print(identifier)
    return render(request,'analysis/importexcel.html',{})

def charts(request):
    return render(request,'analysis/charts.html',{})

def data(request):
    dataset = Sale.objects.all()
    data = serializers.serialize('json',dataset)
    return JsonResponse(data, safe=False)
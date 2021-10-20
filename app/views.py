from django.shortcuts import redirect, render
from .models import Record,Detail
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html")

def customers(request):
    detail = Detail.objects.all()
    detailss = {
        'detail':detail
    }
    
    return render(request, "customers.html",detailss)

def transactions(request):
    records = Record.objects.all()
    
    recording = {
        'record':records
    }
    return render(request, "transactions.html", recording)

def transfer(request,event_id):
    detailall = Detail.objects.all()
    detail = detailall.get(clientid = event_id)
    details = {
        'detail':detail,
        'detailall':detailall

    }
    return render(request, "transfer.html",details)

def process(request, event_id):
    try:
        detailall = Detail.objects.all()
        detail = detailall.get(clientid = event_id)
        detail_1 = detailall.get(Name = request.POST['to'])
        details = {
            'detail':detail,
            'detailall':detailall

        }
        if detail.bankbalance >= int(request.POST['amount']):
            detail.bankbalance -= int(request.POST['amount'])
            detail.save()
            detail_1.bankbalance += int(request.POST['amount'])
            detail_1.save()
            messages.success(request,"Successfully Transfered")
        else:
            messages.unsuccess(request,"Bank balance is low")
        record = Record(sendername = detail.Name, receivername = request.POST['to'],amount = int(request.POST['amount']))
        record.save()
    except Exception as e:
        messages.success(request,"Enter the valid values")
    return render(request, "transfer.html",details)

from django.shortcuts import render, redirect
from .forms import WorkorderForm
from django.http import HttpResponseRedirect
from .models import Workorder
from django.contrib import messages
#from .models import Inputitem

def add_workorder(request):
    submitted = False
    if request.method == "POST":
        form = WorkorderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/workorders/add_workorder?submitted=True')
    else:
        form = WorkorderForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'workorders/add_workorder.html',{'form':form, 'submitted':submitted})

def all_workorders(request):
    workorder_list = Workorder.objects.all().order_by('workorder')
    return render(request, 'workorders/workorder_list.html',
        {'workorder_list': workorder_list})

def workorder_detail(request, workorder_id):
    workorder_info = Workorder.objects.get(pk=workorder_id)
    return render(request, 'workorders/workorder_detail.html',
        {'workorder_info': workorder_info,})

def workorder_update(request, workorder_id):
    workorder_info = Workorder.objects.get(pk=workorder_id)
    update_form = WorkorderForm(request.POST or None, instance=workorder_info)
    if update_form.is_valid():
        update_form.save()
        return redirect('list-workorders')
    return render(request, 'workorders/update_workorder.html',
        {
        'workorder_info': workorder_info,
        'update_form': update_form,
        })

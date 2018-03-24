from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import Port, Time
import time

# Create your views here.
def get_id(request,id):
    try:
        Port.objects.get(pk=id)
        data = Port.objects.get(pk=id)
        response = JsonResponse({'id': data.id, 'name': data.port_name, 'type': data.port_type, 'state': data.port_state, 'change': data.is_change})
        #Port.objects.filter(pk=id).update(is_change=0)
        return response
    except:
        return HttpResponse(status=404)

def get_name(request,name):
    try:
        Port.objects.get(port_name=name)
        data = Port.objects.get(port_name=name)
        response = JsonResponse({'id': data.id, 'name': data.port_name, 'type': data.port_type, 'state': data.port_state})
        return response
    except:
        return HttpResponse(status=404)

def get_time(request):
    now = int(time.strftime("%H%M", time.localtime()))
    response = JsonResponse({'time': now})
    return response

def i_change_status(requests, id, status):
    try:
        port = Port.objects.get(pk=id)
        if port.port_state == status:
            return HttpResponse(status=403)
        else:
            Port.objects.filter(pk=id).update(port_state=status)
            Port.objects.filter(pk=id).update(is_change=1)
            return HttpResponse(status=200)
    except:
        return HttpResponse(status=404)

def n_change_status(requests,name,status):
    try:
        port = Port.objects.get(port_name=name)
        if port.port_state == status:
            return HttpResponse(status=403)
        else:
            Port.objects.filter(port_name=name).update(port_state=status)
            Port.objects.filter(port_name=name).update(is_change=1)
            return HttpResponse(status=200)
    except:
        return HttpResponse(status=404)

def get_is_change(request):
    response = {}
    i = 0
    for obj in Port.objects.filter(is_change=1):
        response[i] = obj.id
        i += 1
    return JsonResponse(response)

def update_is_change(request,id):
    try:
        Port.objects.get(pk=id)
        Port.objects.filter(pk=id).update(is_change=0)
        return HttpResponse(status=403)
    except:
        return HttpResponse(status=404)

def time_c(request):
    now = int(time.strftime("%H%M", time.localtime()))
    for obj in Time.objects.filter(ctrl=1, s_time__lte=now, is_change=0):
        port = obj.port_id
        Port.objects.filter(pk=port, port_type=0).update(port_state=1, is_change=1)
        Time.objects.filter(port_id=port).update(is_change=1)
    # #
    for obj in Time.objects.filter(ctrl=1, c_time__lte=now, is_change=1):
        port = obj.port_id
        Port.objects.filter(pk=port, port_type=0).update(port_state=0, is_change=1)
        Time.objects.filter(port_id=port).update(is_change=0)
    Time.objects.filter(ctrl=1, loop=0, c_time__lt=now).delete()
    return HttpResponse(status=403)

def add_time_c(request):
    try:
        s_time = request.GET.get('st')
        c_time = request.GET.get('ct')
        id = request.GET.get('id')
        loop = request.GET.get('loop')
        Time.objects.create(port_id=id, ctrl=1, loop=loop, s_time=s_time, c_time=c_time, is_change=0)
        return HttpResponse(status=403)
    except:
        return HttpResponse(status=404)
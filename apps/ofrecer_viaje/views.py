from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from apps.ofrecer_viaje.forms import ofrecerviajeForm
from apps.ofrecer_viaje.models import ofrecer_viaje
# Create your views here.

def index(request):
    return render(request, "ofrecer_viaje/index.html")

def ofrecer_viaje_view(request):
    if request.method == 'POST':
        form = ofrecerviajeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ofrecerviaje:listar_viaje')
    else:
        form = ofrecerviajeForm()

    return render(request, 'ofrecer_viaje/ofrecerviaje_form.html',{'form': form})

def ofrecerviaje_list(request):
    ofrecerviaje = ofrecer_viaje.objects.all().order_by('id')
    contexto = {'viajes': ofrecerviaje}
    return render (request, 'ofrecer_viaje/ofrecerviaje_list.html', contexto)

def ofrecerviaje_edit(request, id_ofrecerviaje):
    ofrecerviaje = ofrecer_viaje.objects.get(id=id_ofrecerviaje)
    if request.method == 'GET':
        form = ofrecerviajeForm(instance = ofrecerviaje)
        return render (request.POST,'ofrecer_viaje/ofrecerviaje_form.html',{'form':form})
    if request.method == "POST":
        form = ofrecerviajeForm(request.POST, instance=ofrecerviaje)
        if form.is_valid():
            form.save()
    return redirect('listar_viaje')

def ofrecerviaje_delete(request, id_ofrecerviaje):
    ofrecerviaje = ofrecer_viaje.objects.get(id= id_ofrecerviaje)
    if request.method == 'POST':
        ofrecerviaje.delete()
        return redirect('viaje_eliminar')
    return render(request, 'ofrecer_viaje/ofrecerviaje_delete.html', {'ofrecerviaje' :ofrecerviaje})


class ofrecerviajelist(ListView):
    model = ofrecer_viaje
    template_name = 'ofrecer_viaje/ofrecerviaje_list.html'

class ofrecerviajecreate(CreateView):
    model = ofrecer_viaje
    form_class = ofrecerviajeForm
    template_name = 'ofrecer_viaje/ofrecerviaje_form.html'
    success_url = reverse_lazy('ofrecerviaje:crear_viaje')

class ofrecerviajeupdate(UpdateView):
    model = ofrecer_viaje
    form_class = ofrecerviajeForm
    template_name = 'ofrecer_viaje/ofrecerviaje_form.html'
    success_url = reverse_lazy('ofrecerviaje:crear_viaje')

class ofrecerviajedelete(DeleteView):
    model = ofrecer_viaje
    template_name = 'ofrecer_viaje/ofrecerviaje_delete.html'
    success_url = reverse_lazy('ofrecerviaje:listar_viaje')
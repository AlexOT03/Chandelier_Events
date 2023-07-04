from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .form import StateForm
from .models import State

# Create your views here.
class statePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        states = State.objects.all().order_by('id')
        form_state = StateForm()
        
        return render(request, 'state.html', {
            'states': states,
            'form_state': form_state,
        })
    
    def post(self, request, *args, **kwargs):
        states = State.objects.all().order_by('id')
        form_state = StateForm(request.POST, request.FILES)
        
        if form_state.is_valid():
            form_state.save()
        else:
            return render(request, 'state.html', {
                'states': states,
                'form_state': form_state,
            })
            
        return redirect('state_admin')
    
    def show(self, request, id, **kwargs):
        state = State.objects.get(id=id)
        
        return render(request, 'state_info.html', {
            'state': state,
        })
    
    def update(self, request, id, **kwargs):
        state = State.objects.get(id=id)
        
        if request.method == 'POST':
            form_state = StateForm(request.POST, request.FILES, instance=state)
            
            if form_state.is_valid():
                form_state.save()
                return redirect('state_admin') 
        else:
            form_state = StateForm(instance=state)
                
        return render(request, 'state_edit.html', {
            'state': state,
            'form_state': form_state,
        })
    
    def delete(self, request, id, **kwargs):
        state = State.objects.get(id=id)
        state.delete()
        
        return redirect('state_admin')
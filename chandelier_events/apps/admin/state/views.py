from django.shortcuts import render,redirect
from django.views import View
from .form import StateForm
from .models import State

# Create your views here.
class statePageView(View):
    def get(self, request, *args, **kwargs):
        states = State.objects.all()
        form_state = StateForm()
        
        return render(request, 'state.html', {
            'states': states,
            'form_state': form_state,
        })
    
    def post(self, request, *args, **kwargs):
        return redirect('state_admin')
    
    def show(self, request, *args, **kwargs):
        return render(request, 'state_info.html')
    
    def update(self, request, *args, **kwargs):
        return redirect('state_admin')
    
    def delete(self, request, *args, **kwargs):
        return redirect('state_admin')
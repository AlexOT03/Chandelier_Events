from chandelier_events.apps.admin.theme.models import Theme
from chandelier_events.apps.admin.state.models import State

def themes(request):
    themes = Theme.objects.all()
    return {'themes': themes}

def states(request):
    states = State.objects.all()
    return {'states': states}
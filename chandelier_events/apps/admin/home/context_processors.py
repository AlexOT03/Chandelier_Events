from chandelier_events.apps.user.message.models import Message
from chandelier_events.apps.admin.quote.models import Quote

def messages(request):
    messages = Message.objects.all()
    return {'messages': messages}

def quotes(request):
    quotes = Quote.objects.all()
    return {'quotes': quotes}
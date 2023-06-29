from chandelier_events.apps.user.message.models import Message

def messages(request):
    messages = Message.objects.all()
    return {'messages': messages}
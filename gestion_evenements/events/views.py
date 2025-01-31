from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Event, Participant
from .forms import EventForm
from django.contrib.auth import login

def home(request):
    return render(request, 'events/home.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    is_participant = event.participant_set.filter(user=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'events/event_detail.html', {'event': event, 'is_participant': is_participant})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id, created_by=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id, created_by=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

@login_required
def join_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Participant.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', event_id=event.id)

@login_required
def leave_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Participant.objects.filter(user=request.user, event=event).delete()
    return redirect('event_detail', event_id=event.id)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_events(request):
    events = request.user.events.all() 
    return render(request, 'user/user_events.html', {'events': events})
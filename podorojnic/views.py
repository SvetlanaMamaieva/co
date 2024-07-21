from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from  .models import Direction, Entry
from .forms import DirectionForm, EntryForm, SimpleForm
def index(request):
    return render(request, 'podorojnic/index.html')



def directions(request):
    # directions = Direction.objects.filter(owner=request.user).order_by('date_added')
    directions = Direction.objects.order_by('date_added')
    context = {'directions':directions}
    return render(request,
    'podorojnic/directions.html',
    context=context
    )
@login_required
def direction(request, direction_id):
    direction = Direction.objects.get(id=direction_id)
    if direction.owner != request.user:
        raise Http404
    entries = direction.entry_set.order_by('-date_added')
    context = {'direction':direction, 'entries': entries}
    return render(request,
    'podorojnic/direction.html',
    context=context
    )

@login_required

def new_direction(request):
    if request.method == 'POST':
        form = DirectionForm(request.POST)
        if form.is_valid():
            direction = form.save(commit=False)
            direction.owner = request.user  # Set the owner to the current logged-in user
            direction.save()

            return redirect('podorojnic:directions')

    else:
        form = DirectionForm()

    context = {'form': form}
    return render(request, 'podorojnic/new_direction.html', context)

@login_required
def new_entry(request, direction_id):
    direction = Direction.objects.get(id=direction_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.direction = direction
            new_entry.save()
            return redirect('podorojnic:direction', direction_id=direction_id)

    context = {'direction':direction, 'form': form }
    return render(request, 'podorojnic/new_entry.html', context=context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    direction = entry.direction
    if direction.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('podorojnic:direction', direction_id=direction.id)

    context = {'direction':direction, 'form': form, 'entry': entry}
    return render(
        request,
        'podorojnic/edit_entry.html',
        context=context
    )

def best_co(request):
    return render(request, 'podorojnic/best_co.html')

def simple_from_view(request):
    form = SimpleForm()
    return render(
       request,
        'podorojnic/simple_from_view.html',
        context={'form':form}
    )


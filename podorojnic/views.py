from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from  .models import Direction, Entry, Country, Info
from .forms import DirectionForm, EntryForm, CountryForm, InfoForm

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

def countries(request):
    # directions = Direction.objects.filter(owner=request.user).order_by('date_added')
    countries = Country.objects.order_by('date_added')
    context = {'countries': countries}
    return render(request,
    'podorojnic/countries.html',
    context=context
    )

@login_required
def country(request, country_id):
    country = Country.objects.get(id=country_id)
    if country.owner != request.user:
        raise Http404
    infos = country.info_set.order_by('-date_added')
    context = {'country':country, 'infos': infos}
    return render(request,
    'podorojnic/countries.html',
    context=context
    )


@login_required
def new_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save(commit=False)
            country.owner = request.user
            country.save()
            return redirect('podorojnic:countries')
    else:
        form = CountryForm()
    countries = Country.objects.all()
    context = {'form': form}
    return render(request,
   'podorojnic/new_country.html', {'form':form, 'countries':countries})



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


@login_required
def new_info(request, country_id):
    country = Country.objects.get(id=country_id)
    if request.method != 'POST':
        form = InfoForm()
    else:
        form = InfoForm(request.POST)
        if form.is_valid():
            new_info = form.save(commit=False)
            new_info.country = country
            new_info.save()
            return redirect('podorojnic:country', country_id=country_id)

    context = {'country':country, 'form': form }
    return render(request, 'podorojnic/new_info.html', context=context)


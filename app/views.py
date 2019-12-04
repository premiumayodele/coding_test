from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import View
from app.forms import HyphForm, TrailingForm


def consect(request):
    if request.method == 'POST':
        form = HyphForm(request.POST or None)
        if form.is_valid():
            htext = form.cleaned_data['hyphvalue']
            a = int(''.join(filter(str.isdigit, htext)))
            w = [int(digit) for digit in str(a)]
            result = consecutive(w)
            context = {'resp': htext, 'result': result}
            return render(request, 'consecutive.html', context)
        else:
            return redirect('sec')
    else:
        form = HyphForm()
        context = {'form': form}
        return render(request, 'consecutive.html', context)

def trail(request):
    if request.method == 'POST':
        form = TrailingForm(request.POST or None)
        if form.is_valid():
            trtext = request.POST.get('trailtext')
            result = trail_count(int(trtext))
            context = {'resp': trtext, 'result': result}
            return render(request, 'trailing.html', context)
        else:
            return redirect('sec')
    else:
        form = TrailingForm()
        context = {'form': form}
        return render(request, 'trailing.html', context)


def consecutive(var):
    for x in range(2, len(var)):
        forward = var[x] - var[x-1]
        backward = var[x-1] - var[x-2]
    if forward == backward:
        return True
    else:
        return False

def trail_count(x):
    i = 5
    zeros = 0
    while x >= i:
        zeros += x // i
        i *= 5
    return zeros

def home(request):
    return render(request, 'index.html')








def prod(request):
    return HttpResponse("I am working as expected")

def sec(request):
    return HttpResponse("I am working as expected")
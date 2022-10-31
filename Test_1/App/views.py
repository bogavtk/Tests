from django.shortcuts import render, redirect
from .form import AppForm
from .models import Calc_History


def get_truth(symbol, a, b):
    oops = {'*': lambda a, b: a * b,
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '/': lambda a, b: a // b
            }
    return oops[symbol](a, b)


def calculate(request):
    form = AppForm()
    if request.method == 'POST':
        symbol = str(request.POST.get('operator'))
        val1 = int(request.POST.get('val1'))
        val2 = int(request.POST.get('val2'))
        result = get_truth(symbol, val1, val2)
        form = AppForm(request.POST, initial={'result': result})
        if form.is_valid():
            form.save()
            return redirect('calculate')
    return render(request, template_name='App/index.html', context={'form': form})


def history_objects(request):
    storage = Calc_History.objects.all()
    return render(request, "App/obj.html", context={'storage': storage})

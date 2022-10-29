from django.shortcuts import render
from .form import AppForm
from _ast import operator
from django.http import HttpResponse


def get_true(inp, relate, cut):
    ops = {
        '*': operator.mul(),
        '/': operator.truediv(),
        '+': operator.concat(),
        '-': operator.sub()
    }

    return ops[relate](inp, cut)


def find_value(request):
    form = AppForm()
    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            result = get_true(request.POST['val1'], request.POST['operator'], request.POST['val2'])
            form = AppForm(request.POST, initial={'result': result})
            form.save()
            return HttpResponse(result)

    return render(request, template_name='App/index.html', context={'form': form})

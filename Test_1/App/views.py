from django.shortcuts import render
from .form import AppForm
from _ast import operator
from django.http import HttpResponse


def get_true(inp, relate, cut):
    ops = {
        '*': operator.mul,
        '/': operator.truediv,
        '+': operator.concat,
        '-': operator.sub
    }

    return ops[relate](inp, cut)


def find_value(request):
    form = AppForm()
    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            add_result = get_true(form.val1, form.operator, form.val2)
            result = f'{form.val1}{operator}{form.val2} = {add_result}'
            form = AppForm(request.POST, initial={'result': add_result})
            form.save()

            create_ob = AppForm.objects.create(form, result=add_result)
            return HttpResponse(result)

    return render(request, template_name='App/index.html', context={'form': form})

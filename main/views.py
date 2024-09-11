from django.shortcuts import render
def show_main(request):
    context = {
        'name' : 'Priyapta Naufal Sudrajat',
        'npm': '2306245106',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
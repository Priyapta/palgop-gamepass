from django.shortcuts import render
def show_main(request):
    context = {
        'itemName' : 'Priyapta Naufal Sudrajat',
        'itemPrice': '2306245106',
        'itemDescription': 'PBP D'
    }

    return render(request, "main.html", context)
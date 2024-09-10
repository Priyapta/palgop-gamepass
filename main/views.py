from django.shortcuts import render
def show_main(request):
    context = {
        'itemName' : '2306123456',
        'itemPrice': 'Pak Bepe',
        'itemDescription': 'PBP E'
    }

    return render(request, "main.html", context)
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Mahira Irgiani',
        'class': 'PBP E',
        'amount_books': '12',
    }

    return render(request, "main.html", context)
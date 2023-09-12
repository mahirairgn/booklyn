from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Mahira Irgiani',
        'class': 'PBP E',
        'total_amount': '12',
    }

    return render(request, "main.html", context)
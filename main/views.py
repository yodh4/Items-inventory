from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'The Lord of the Rings: The Return of the King',
        'amount': '3',
        'description' : 'Film kedua dari series The Lord of the Rings' 
    }

    return render(request, "main.html", context)
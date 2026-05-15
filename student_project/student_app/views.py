from django.shortcuts import render

# Create your views here.

# def indexPage(request):
#     return render(request, 'index.html')

def indexPage(request):
    return render(request, 'index.html')


def favplayerPage(request):
    data={
        "name":"Jonathan",
        "age": 23,
        "gender": "Male",
        "country": "India",
        "game": "PUBG",
        "team": "Apex Gaming",
    }
    return render(request, 'favplayer.html', data)
from django.shortcuts import render

# Create your views here.

# def favmoviePage(request):
#     return render(request, 'favmovies')

# def directorPage(request):
#     return render(request, 'director.html')

def indexPage(request):
    return render(request, 'index.html')


def favmoviePage(request):
    data={
        "tittle": "Dhurander-The Revenge",
        "year": 2026,
        "genre": "Spy Thriller-Action",
        "Director": "Aditya Dhar",
        "Rating": 5,

    }
    return render(request, 'favmovies.html', data)


def directorPage(request):
    data={
        "name": "Aditya Dhar",
        "profession": "Director", 
        "debut": "Uri",
        "spouce": "Yami Gautam",
    }
    return render(request, 'director.html', data)
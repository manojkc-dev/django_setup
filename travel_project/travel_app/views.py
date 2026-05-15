from django.shortcuts import render

# Create your views here.

def indexPage(request):
    return render(request, 'index.html')

def nepalPage(request):
    data={
        "name": "Nepal",
        "capital":"Kathmandu",
        "famous":"Sagarmatha",
        "president":"Ram Chandra Paudel",
        "currency":"Neplese Rupee",
    }
    return render(request, 'nepal.html', data)


def indiaPage(request):
    data={
        "name": "India",
        "capital":"Delhi",
        "famous":"Taj Mahal",
        "president":"Droupadi Murmu",
        "currency":"Indian Rupee",
    }
    return render(request, 'india.html', data)


def chinaPage(request):
    data={
        "name": "China",
        "capital":"Beijing",
        "famous":"Great Wall of China",
        "president":"Xi Jinping",
        "currency":"Chinese Yuan",
    }
    return render(request, 'china.html', data)


def usaPage(request):
    data={
        "name": "United States of America",
        "capital":"Washington",
        "famous":"Statue of Liberty",
        "president":"Joe Biden",
        "currency":"USD",
    }
    return render(request, 'usa.html', data)


def japanPage(request):
    data={
        "name": "Japan",
        "capital":"Tokyo",
        "famous":"Mount Fuji",
        "president":"Emperor Naruhito",
        "currency":"Yen",
    }
    return render(request, 'japan.html', data)
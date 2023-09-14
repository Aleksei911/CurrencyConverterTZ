import requests
from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        return render(request, 'main/index.html')
    else:
        val = request.POST['amount']
        cur1 = request.POST['cur1']
        cur2 = request.POST['cur2']

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur2}&from={cur1}&amount={val}"

        payload = {}
        headers = {
            "apikey": "Ioxl2weReBDLWMpZuAURiRtuYAqTxImz"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()

        context = {
            'to_convert': result['query']['to'],
            'from_convert': result['query']['from'],
            'amount': result['query']['amount'],
            'result': round(result['result'], 2),
        }

        return render(request, 'main/index.html', context)

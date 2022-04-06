

def get_invoices(from_date='2022-01-01', to_date='2022-01-31'):
    import requests
    import json

    url = "https://api.robolabs.lt/api/get_invoice_list/"

    payload = json.dumps({
        "secret": "SECRET",
        "date_from": f"{from_date} 00:00:00",
        "date_to": f"{to_date} 00:00:00",
        "execute_immediately": True
    })
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json().get('result').get('data')
    return []
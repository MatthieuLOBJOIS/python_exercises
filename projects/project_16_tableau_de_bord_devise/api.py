from datetime import date, timedelta
from pprint import pprint

import requests

def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)
    r = requests.get(f"https://www.docstring.fr/api/rates/history/?start_at={start_date}&end_at={end_date}&symbols={','.join(currencies)}")
    
    if not r and not r.json():
        return False, False
    
    api_rates = r.json().get("rates")
    pprint(api_rates)
    return None, None

if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "CAD"])

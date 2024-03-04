import requests

def currencyConverter(eur_amount):
    USDCNY = "USDCNY"
    EURUSD = "EURUSD"
    URLUSD = "https://www.freeforexapi.com/api/live?pairs=" + USDCNY
    URLEUR = "https://www.freeforexapi.com/api/live?pairs=" + EURUSD
    usd_amount = None

    # Get the exchange rate from USD to EUR
    EUR_response = requests.get(URLEUR)
    if EUR_response.status_code == 200:
        try:
            response_json = EUR_response.json()
            if 'message' not in response_json:
                rate_usd = str(response_json["rates"][EURUSD]["rate"])
                usd_amount = float(eur_amount) * float(rate_usd)
                #print("EUR -> USD:", str(usd_amount))
            else:
                print("Currency pair not found in response:", EURUSD)
        except Exception as e:
            print("Error:", e)
    else:
        print("Request for EUR currency converter failed with status code", EUR_response.status_code)

    # Get the exchange rate from CNY to USD
    USD_response = requests.get(URLUSD)
    if USD_response.status_code == 200:
        try:
            response_json = USD_response.json()
            if 'message' not in response_json:
                rate_cny = str(response_json["rates"][USDCNY]["rate"])
                cny_amount = usd_amount * float(rate_cny)
                #print("USD -> CNY:", str(cny_amount))
            else:
                print("Currency pair not found in response:", USDCNY)
        except Exception as e:
            print("Error:", e)
    else:
        print("Request for USD currency converter failed with status code", USD_response.status_code)

    return round(cny_amount, 2)


#if __name__ == '__main__':
#    print(currencyConverter(50.82))


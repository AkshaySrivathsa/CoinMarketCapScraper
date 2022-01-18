from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")


def get_data():

    n = int(input('type the number of cryptocurrencies to be mined(Max. 10): '))

    t_body = doc.tbody
    trs = t_body.contents

    prices = {}
    names = []
    price = []
    marketCap = []
    volume = []
    short_names = []

    for tr in trs[:n]:
        name, _price = tr.contents[2:4]
        fixed_name = name.p.string
        fixed_price = _price.a.string
        prices[fixed_name] = fixed_price
        market_cap, _volume = tr.contents[6:8]
        marketCap.append(float(str(market_cap.span.string).replace('$', '').replace('B', '')))
        volume.append(int(str(_volume.a.string).replace('$', '').replace(',', '')))
        names.append(name.p.string)
        short_names.append(str(name.p.string)[:3].upper())
        price.append(float(str(_price.a.string).replace('$', '').replace(',', '')))

    for key in prices:
        value = prices[key]
        print(f"{key}: {value}")

    left = [i for i in range(1, n + 1)]

    plt.bar(left, price, tick_label=short_names, width=0.8, color=['red', 'green'])
    plt.xlabel('Cryptocurrencies')
    plt.ylabel('prices of cryptocurrencies')
    plt.title('Crypto Price Comparison')
    plt.show()

    plt.bar(left, marketCap, tick_label=short_names, width=0.8, color=['red', 'green'])
    plt.xlabel('Cryptocurrencies')
    plt.ylabel('marketCapitals of cryptocurrencies')
    plt.title('Crypto marketCapital Comparison')
    plt.show()

    plt.bar(left, volume, tick_label=short_names, width=0.8, color=['red', 'green'])
    plt.xlabel('Cryptocurrencies')
    plt.ylabel('volume of cryptocurrencies')
    plt.title('Crypto Volume Comparison')
    plt.show()


if __name__ == "__main__":
    get_data()

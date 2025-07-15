import requests
from bs4 import BeautifulSoup

def fetch_exchange_rates():
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"  # 台灣銀行匯率
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    # 結果 dict
    rates = {}

    # 找到匯率表格
    table = soup.find("table", {"title": "牌告匯率"})
    rows = table.find("tbody").find_all("tr")

    # 只抓幾個幣別
    wanted_currencies = {
        "日圓 (JPY)": "JPY",
        "美金 (USD)": "USD",
        "歐元 (EUR)": "EUR"
    }

    for row in rows:
        currency_name = row.find("div", class_="visible-phone").get_text(strip=True)
        # print(f"抓到的幣別名稱: {currency_name}")
        if currency_name in wanted_currencies:
            tds = row.find_all("td")
            spot_buy = tds[2].get_text(strip=True)
            # spot_buy 是字串，需要轉成 float
            spot_buy_value = float(spot_buy.replace(",", ""))
            rates[wanted_currencies[currency_name]] = {"spot_buy": spot_buy_value}

    return rates

if __name__ == "__main__":
    # 測試
    data = fetch_exchange_rates()
    print(data)
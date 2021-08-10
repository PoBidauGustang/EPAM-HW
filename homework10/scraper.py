#!/usr/bin/python3
import asyncio
import json

# import time
import xml.etree.ElementTree as ET
from typing import List

import aiohttp
import requests
from bs4 import BeautifulSoup

# start_time = time.time()


url1 = "http://www.cbr.ru/scripts/XML_daily.asp"
response1 = requests.get(url1)
root1 = ET.fromstring(response1.text)

dollar_in_rubles = root1[10][4].text
dollar_in_rubles = float(dollar_in_rubles.replace(",", "."))

urls = [
    f"https://markets.businessinsider.com/index/components/s&p_500?p={i}"
    for i in range(1, 12)
]


async def request_controller(urls: List[str]) -> List:
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(request_worker(session, url)) for url in urls]
        return await asyncio.gather(*tasks)


async def request_worker(session: aiohttp.client.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


ioloop = asyncio.get_event_loop()
table_SP_500 = ioloop.run_until_complete(request_controller(urls))


company_names = []
company_links = []
company_year_growth = []

for page in table_SP_500:
    soup = BeautifulSoup(page, "lxml")

    a_title_href_tags = soup.select("tbody tr td a[title]")
    for tag in a_title_href_tags:
        company_name = tag["title"]
        company_names.append(company_name)
        link = tag.get("href")
        company_links.append("https://markets.businessinsider.com" + link)

    growth_data_tags = soup.select("tbody tr td span")[9::10]
    for tag in growth_data_tags:
        company_year_growth.append(tag.getText())

ioloop = asyncio.get_event_loop()
company_pages = ioloop.run_until_complete(request_controller(company_links))

share_prices = []
company_codes = []
p_e_ratios = []
lost_profits = []

for company_page in company_pages:
    soup = BeautifulSoup(company_page, "lxml")

    share_price_in_dollars = float(
        soup.find(class_="price-section__current-value").getText().replace(",", "")
    )
    share_price_in_roubles = share_price_in_dollars * dollar_in_rubles
    share_prices.append(round(share_price_in_roubles, 4))

    company_code = soup.select_one("h1 span span").getText().replace(", ", "")
    company_codes.append(company_code)

    p_e_ratio_raw = soup.select(".snapshot .snapshot__data-item")[6].getText()
    p_e_ratio = float(p_e_ratio_raw.strip().split()[0].replace(",", ""))
    p_e_ratios.append(p_e_ratio)

    week_low_52_raw = soup.select(".snapshot .snapshot__data-item")[4].getText()
    week_low_52 = float(week_low_52_raw.strip().split()[0].replace(",", ""))
    week_high_52_raw = soup.select(".snapshot .snapshot__data-item")[5].getText()
    week_high_52 = float(week_high_52_raw.strip().split()[0].replace(",", ""))

    lost_profit = (week_high_52 - week_low_52) / week_low_52
    lost_profit_in_percents = f"{round((lost_profit * 100), 2)}%"
    lost_profits.append(lost_profit_in_percents)

collected_data = []

for name, link, share_price, code, p_e, growth, profit in zip(
    company_names,
    company_links,
    share_prices,
    company_codes,
    p_e_ratios,
    company_year_growth,
    lost_profits,
):
    company_dict = {
        "name": name,
        "link": link,
        "share price": share_price,
        "code": code,
        "P/E": p_e,
        "growth": growth,
        "lost profit": profit,
    }
    collected_data.append(company_dict)

top_10_expensive_stocks = sorted(
    collected_data, key=lambda k: k["share price"], reverse=True
)[:10]
with open("top_10_expensive_shares.txt", "w") as outfile:
    json.dump(top_10_expensive_stocks, outfile, indent=4)


top_10_lowest_p_e_ratio = sorted(collected_data, key=lambda k: k["P/E"])[:10]
with open("top_10_lowest_p_e_ratio.txt", "w") as outfile:
    json.dump(top_10_lowest_p_e_ratio, outfile, indent=4)


top_10_highest_growth = sorted(collected_data, key=lambda k: k["growth"], reverse=True)[
    :10
]
with open("top_10_highest_growth.txt", "w") as outfile:
    json.dump(top_10_highest_growth, outfile, indent=4)


top_10_highest_potential_profit = sorted(
    collected_data, key=lambda k: k["lost profit"], reverse=True
)[:10]
with open("top_10_highest_lost_profit.txt", "w") as outfile:
    json.dump(top_10_highest_potential_profit, outfile, indent=4)

# print(f"Process took {time.time() - start_time}")

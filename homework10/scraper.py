#!/usr/bin/python3
import asyncio
import json
import time
import xml.etree.ElementTree as ET
from typing import Callable, Generator, List, Union

import aiohttp
import requests
from bs4 import BeautifulSoup

start_time = time.time()

url_currencies = "http://www.cbr.ru/scripts/XML_daily.asp"


def get_dollar_in_rubles(url: str) -> float:

    response = requests.get(url)
    root = ET.fromstring(response.text)

    dollar_in_rubles = root[10][4].text
    return float(dollar_in_rubles.replace(",", "."))


urls = [
    f"https://markets.businessinsider.com/index/components/s&p_500?p={i}"
    for i in range(1, 12)
]


async def request_controller(urls: Union[list, Generator[str, None, None]]) -> List:
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(request_worker(session, url)) for url in urls]
        return await asyncio.gather(*tasks)


async def request_worker(session: aiohttp.client.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


def get_table_SP_500_async() -> List[str]:
    ioloop = asyncio.get_event_loop()
    return ioloop.run_until_complete(request_controller(urls))


def get_table_SP_500_text(pages: list) -> Generator[BeautifulSoup, None, None]:
    for page in pages:
        yield BeautifulSoup(page, "lxml")


pages_text = list(get_table_SP_500_text(get_table_SP_500_async()))


def get_company_names(pages: List[BeautifulSoup]) -> Generator[str, None, None]:
    for page in pages:
        a_title_href_tags = page.select("tbody tr td a[title]")
        for tag in a_title_href_tags:
            company_name = tag["title"]
            yield company_name


def get_company_links(pages: List[BeautifulSoup]) -> Generator[str, None, None]:
    for page in pages:
        a_title_href_tags = page.select("tbody tr td a[title]")
        for tag in a_title_href_tags:
            link = tag.get("href")
            yield ("https://markets.businessinsider.com" + link)


def get_year_growth(pages: List[BeautifulSoup]) -> Generator[str, None, None]:
    for page in pages:
        growth_data_tags = page.select("tbody tr td span")[9::10]
        for tag in growth_data_tags:
            yield tag.getText()


def get_company_pages_async() -> List[str]:
    ioloop = asyncio.get_event_loop()
    return ioloop.run_until_complete(request_controller(get_company_links(pages_text)))


def get_company_pages(pages: list) -> Generator[BeautifulSoup, None, None]:
    for page in pages:
        yield BeautifulSoup(page, "lxml")


company_pages_text = get_company_pages(get_company_pages_async())


def get_share_prices(
    pages: Generator[BeautifulSoup, None, None]
) -> Generator[float, None, None]:
    for company_page in pages:
        share_price_in_dollars = float(
            company_page.find(class_="price-section__current-value")
            .getText()
            .replace(",", "")
        )
        share_price_in_roubles = share_price_in_dollars * get_dollar_in_rubles(
            url_currencies
        )
        yield round(share_price_in_roubles, 4)


def get_company_codes(
    pages: Generator[BeautifulSoup, None, None]
) -> Generator[str, None, None]:
    for company_page in pages:
        yield company_page.select_one("h1 span span").getText().replace(", ", "")


def get_p_e_ratios(
    pages: Generator[BeautifulSoup, None, None]
) -> Generator[str, None, None]:
    for company_page in pages:
        p_e_ratio_raw = company_page.select(".snapshot .snapshot__data-item")[
            6
        ].getText()
        yield float(p_e_ratio_raw.strip().split()[0].replace(",", ""))


def get_lost_profits(
    pages: Generator[BeautifulSoup, None, None]
) -> Generator[str, None, None]:
    for company_page in pages:
        week_low_52_raw = company_page.select(".snapshot .snapshot__data-item")[
            4
        ].getText()
        week_low_52 = float(week_low_52_raw.strip().split()[0].replace(",", ""))
        week_high_52_raw = company_page.select(".snapshot .snapshot__data-item")[
            5
        ].getText()
        week_high_52 = float(week_high_52_raw.strip().split()[0].replace(",", ""))

        lost_profit = (week_high_52 - week_low_52) / week_low_52
        lost_profit_in_percents = f"{round((lost_profit * 100), 2)}%"
        yield lost_profit_in_percents


def get_collected_data(
    company_names: Callable,
    company_links: Callable,
    share_prices: Callable,
    company_codes: Callable,
    p_e_ratios: Callable,
    year_growth: Callable,
    lost_profits: Callable,
) -> Generator[dict, None, None]:
    for name, link, share_price, code, p_e, growth, profit in zip(
        company_names,
        company_links,
        share_prices,
        company_codes,
        p_e_ratios,
        year_growth,
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
        yield company_dict


collected_data = list(
    get_collected_data(
        get_company_names(pages_text),
        get_company_links(pages_text),
        get_share_prices(company_pages_text),
        get_company_codes(company_pages_text),
        get_p_e_ratios(company_pages_text),
        get_year_growth(pages_text),
        get_lost_profits(company_pages_text),
    )
)


def get_top_10_expensive_stocks(collected_data: List[Callable]) -> None:
    top_10_expensive_stocks = sorted(
        collected_data, key=lambda k: k["share price"], reverse=True
    )[:10]
    with open("top_10_expensive_shares.txt", "w") as outfile:
        json.dump(top_10_expensive_stocks, outfile, indent=4)


def get_top_10_lowest_p_e_ratio(collected_data: List[Callable]) -> None:
    top_10_lowest_p_e_ratio = sorted(collected_data, key=lambda k: k["P/E"])[:10]
    with open("top_10_lowest_p_e_ratio.txt", "w") as outfile:
        json.dump(top_10_lowest_p_e_ratio, outfile, indent=4)


def get_top_10_highest_growth(collected_data: List[Callable]) -> None:
    top_10_highest_growth = sorted(
        collected_data, key=lambda k: k["growth"], reverse=True
    )[:10]
    with open("top_10_highest_growth.txt", "w") as outfile:
        json.dump(top_10_highest_growth, outfile, indent=4)


def get_top_10_highest_lost_profit(collected_data: List[Callable]) -> None:
    top_10_highest_lost_profit = sorted(
        collected_data, key=lambda k: k["lost profit"], reverse=True
    )[:10]
    with open("top_10_highest_lost_profit.txt", "w") as outfile:
        json.dump(top_10_highest_lost_profit, outfile, indent=4)


print(f"Process took {time.time() - start_time}")


if __name__ == "__main__":
    get_top_10_expensive_stocks(collected_data)
    get_top_10_lowest_p_e_ratio(collected_data)
    get_top_10_highest_growth(collected_data)
    get_top_10_highest_lost_profit(collected_data)

#!/usr/bin/python3
import asyncio
import json
import xml.etree.ElementTree as ET
from typing import Callable, List

import aiohttp
import requests
from bs4 import BeautifulSoup


def get_dollar_in_rubles(url: str) -> float:

    response = requests.get(url)
    root = ET.fromstring(response.text)

    dollar_in_rubles = root[10][4].text
    return float(dollar_in_rubles.replace(",", "."))


async def request_controller(urls: List[str]) -> List:
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(request_worker(session, url)) for url in urls]
        return await asyncio.gather(*tasks)


async def request_worker(session: aiohttp.client.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


def get_table_SP_500_async() -> List[str]:
    ioloop = asyncio.get_event_loop()
    return ioloop.run_until_complete(request_controller(urls))


def get_table_SP_500_text(pages: list) -> List[BeautifulSoup]:
    pages_text = [BeautifulSoup(page, "lxml") for page in pages]
    return pages_text


def get_company_names(pages: List[BeautifulSoup]) -> List[str]:
    company_names = []
    for page in pages:
        a_title_href_tags = page.select("tbody tr td a[title]")
        company_name_of_page = [tag["title"] for tag in a_title_href_tags]
        company_names.extend(company_name_of_page)
    return company_names


def get_company_links(pages: List[BeautifulSoup]) -> List[str]:
    company_links = []
    for page in pages:
        a_title_href_tags = page.select("tbody tr td a[title]")
        company_link_of_page = [
            "https://markets.businessinsider.com" + tag.get("href")
            for tag in a_title_href_tags
        ]
        company_links.extend(company_link_of_page)
    return company_links


def get_year_growth(pages: List[BeautifulSoup]) -> List[str]:
    year_growth = []
    for page in pages:
        growth_data_tags = page.select("tbody tr td span")[9::10]
        year_growth_of_page = [tag.getText() for tag in growth_data_tags]
        year_growth.extend(year_growth_of_page)
    return year_growth


def get_company_pages_async() -> List[str]:
    ioloop = asyncio.get_event_loop()
    return ioloop.run_until_complete(request_controller(get_company_links(pages_text)))


def get_company_pages(pages: list) -> List[BeautifulSoup]:
    company_pages = [BeautifulSoup(page, "lxml") for page in pages]
    return company_pages


def get_share_prices(pages: List[BeautifulSoup]) -> List[float]:
    share_prices = []
    for company_page in pages:
        share_price_in_dollars = float(
            company_page.find(class_="price-section__current-value")
            .getText()
            .replace(",", "")
        )
        share_price_in_roubles = share_price_in_dollars * get_dollar_in_rubles(
            url_currencies
        )
        share_prices.append(round(share_price_in_roubles, 4))
    return share_prices


def get_company_codes(pages: List[BeautifulSoup]) -> List[str]:
    company_codes = [
        company_page.select_one("h1 span span").getText().replace(", ", "")
        for company_page in pages
    ]
    return company_codes


def get_p_e_ratios(pages: List[BeautifulSoup]) -> List[str]:
    p_e_ratios = []
    for company_page in pages:
        p_e_ratio_raw = company_page.select(".snapshot .snapshot__data-item")[
            6
        ].getText()
        p_e_ratios.append(float(p_e_ratio_raw.strip().split()[0].replace(",", "")))
    return p_e_ratios


def get_lost_profits(pages: List[BeautifulSoup]) -> List[str]:
    lost_profits = []
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
        lost_profits.append(lost_profit_in_percents)
    return lost_profits


def get_collected_data(
    company_names: Callable,
    company_links: Callable,
    share_prices: Callable,
    company_codes: Callable,
    p_e_ratios: Callable,
    year_growth: Callable,
    lost_profits: Callable,
) -> List[dict]:
    collected_data = []
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
        collected_data.append(company_dict)
    return collected_data


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


if __name__ == "__main__":
    url_currencies = "http://www.cbr.ru/scripts/XML_daily.asp"
    urls = [
        f"https://markets.businessinsider.com/index/components/s&p_500?p={i}"
        for i in range(1, 12)
    ]
    pages_text = get_table_SP_500_text(get_table_SP_500_async())
    company_pages_text = get_company_pages(get_company_pages_async())
    collected_data = get_collected_data(
        get_company_names(pages_text),
        get_company_links(pages_text),
        get_share_prices(company_pages_text),
        get_company_codes(company_pages_text),
        get_p_e_ratios(company_pages_text),
        get_year_growth(pages_text),
        get_lost_profits(company_pages_text),
    )

    get_top_10_expensive_stocks(collected_data)
    get_top_10_lowest_p_e_ratio(collected_data)
    get_top_10_highest_growth(collected_data)
    get_top_10_highest_lost_profit(collected_data)

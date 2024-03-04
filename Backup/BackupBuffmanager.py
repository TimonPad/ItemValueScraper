import pandas as pd
import os
import requests
from Classes.SignInSteam import floatpuller
from Classes.currencyconverter import currencyConverter
from Classes.floatselector import floatcategorizer


def BuffPricespull():
    csv_file_path = os.path.abspath('classes/investments.csv')
    df = pd.read_csv(csv_file_path)

    current_lowest_steam_list = []
    current_lowest_buff_list = []
    current_percentage_profit = []
    current_highest_buyorder_list = []
    short_name_list = []
    buy_price_cny_list = []

    for index, row in df.iterrows():
        goods_id = row['goods_id']
        buy_price_cny = currencyConverter(row['buy_price_original'])
        buy_price_cny_list.append(buy_price_cny)
        sell_url = f"https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id={goods_id}&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1"
        buy_url = f"https://buff.163.com/api/market/goods/buy_order?game=csgo&goods_id={goods_id}&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1"
        min_float, max_float = floatcategorizer(row['float_range'])

        sell_response = requests.get(sell_url)
        buy_response = requests.get(buy_url)
        if sell_response.status_code == 200:
            response_data = sell_response.json()
            if "data" in response_data:
                short_name = response_data["data"]["goods_infos"][str(goods_id)]["market_hash_name"]
                steam_price_cny = response_data["data"]["goods_infos"][str(goods_id)]["steam_price_cny"]
                price = floatpuller(goods_id, min_float, max_float)
                if price != float('nan'):
                    percentage_profit = round(((float(price) - float(buy_price_cny)) / float(buy_price_cny)) * 100, 1)
                    current_lowest_buff_list.append(price)
                    current_percentage_profit.append(percentage_profit)
                short_name_list.append(short_name)
                current_lowest_steam_list.append(steam_price_cny)
            else:

                current_lowest_steam_list.append(None)
                current_lowest_buff_list.append(None)
                current_percentage_profit.append(None)
                short_name_list.append(None)
            print(f"Processed Goods ID: {goods_id}")
        else:
            print(f"Failed to fetch data for Goods ID {goods_id}. Status code: {sell_response.status_code}")

        if buy_response.status_code == 200:
            buy_data = buy_response.json()
            current_highest_buyorder = "None"
            if "data" in buy_data:
                items = buy_data["data"].get("items", [])
                if items:
                    current_highest_buyorder = items[0].get("price")
                    if current_highest_buyorder is not None:
                        current_highest_buyorder = "{:.2f}".format(float(current_highest_buyorder))
                current_highest_buyorder_list.append(current_highest_buyorder)
            else:
                print(f"Failed to fetch data for Goods ID {goods_id}. Status code: {buy_response.status_code}")
    df['goods_name'] = short_name_list
    df['current_lowest_steam'] = current_lowest_steam_list
    df['current_lowest_buff'] = current_lowest_buff_list
    df['percentage_profit'] = current_percentage_profit
    df['current_highest_buyorder'] = current_highest_buyorder_list
    df['buy_price_cny'] = buy_price_cny_list
    df.to_csv(csv_file_path, index=False)
import requests
import json
from tkinter import *
from tkinter import ttk


class CryptoViewer:

    def __init__(self, master, pairs):
        self.master = master
        self.pairs = pairs
        self.api_url = 'https://api.binance.com/api/v1/ticker/price'

        self.refresh_btn = ttk.Button(self.master,
                              text='Refresh',
                              command=self.refresh) \
            .grid(row=1, column=0, columnspan=2)
        self.refresh()

    def refresh(self):
        """
        Refresh button callback also used for initial
        data poll.
        """
        recent_data = self.get_current_prices()
        new_values = self.filter_price_list(recent_data, self.pairs)
        self.draw_info_pairs(new_values)

    def get_current_prices(self):
        """
        Call Binance API for most recent price data
        :return: JSON with Binance current exchange rates
        """
        request = requests.get(self.api_url)
        json_response = json.loads(request.text)
        return json_response

    def filter_price_list(self, json_data, pairs):
        """
        Filter the JSON data to have entries only for the predefined pairs
        :return: Filtered list of tuples (symbol,price)
        """
        final_list = []
        for pair in json_data:
            if (pair['symbol'] in pairs and pair['symbol']):
                final_list.append((pair['symbol'], pair['price']))
        return final_list

    def draw_info_pairs(self, list):
        """
        Draw Tkinter window with name:price for the pairs
        :param list: a list of tuple pairs (symbol,price)
        """
        r = 2
        for pair in list:
            ttk.Label(self.master,
                      width=30,
                      text=pair[0] + ' = ' + pair[1],
                      font=('Courier', 18, 'bold')) \
                .grid(row=r, column=1)
            r += 1


def main():
    root = Tk()
    pairs = ('ETHUSDT', 'XLMETH', 'BNBETH', 'XVGETH', 'ARNETH')
    app = CryptoViewer(root, pairs)
    root.mainloop()


if __name__ == '__main__': main()

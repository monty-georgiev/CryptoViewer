import requests
import json
import time
from tkinter import *
from tkinter import ttk


class CryptoCurrency(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    # def say_hello(self, window):
    #     self.window = window
    #     r = 2
    #     total_sum = 0
    #     eth_usd = 0
    #     for pair in list:
    #         pair_sum = pair[2] * pair[1]
    #         if (pair[0] == 'ETHUSDT'):
    #             eth_usd = float(pair[1])
    #         ttk.Label(self.master,
    #                   width=50,
    #                   text="Pair: {} \n Current Price: {} \n Amount: {}  \n Total: {} \n".format(pair[0], pair[1],
    #                                                                                              pair[2],
    #                                                                                              pair_sum),
    #                   font=('Courier', 14, 'bold')) \
    #             .grid(row=r, column=1)
    #         r += 1
    #         total_sum += pair_sum
    #
    #     ttk.Label(self.master,
    #               font=('Courier', 16, 'bold'),
    #               width=50,
    #               text="Total Value: {} in USD {}".format(total_sum, total_sum * eth_usd)) \
    #         .grid(row=r, column=1)


class CryptoViewer(object):

    def __init__(self):
        self.pairs = [('ETHUSDT', 0), ('XLMETH', 609), ('BNBETH', 3), ('XVGETH', 1717), ('ARNETH', 9), ('TNTETH', 490),
                      ('LENDETH', 190), ('MANAETH', 150)]
        self.master = Tk()
        self.api_url = 'https://api.binance.com/api/v1/ticker/price'

        # self.refresh_btn = ttk.Button(self.master,
        #                               text='Refresh',
        #                               command=self.refresh) \
        #     .grid(row=1, column=0, columnspan=2)

        self.refresh()
        self.master.mainloop()

    def refresh(self):
        """
        Refresh button callback also used for initial
        data poll.
        """
        recent_data = self.get_current_prices()
        new_values = self.filter_price_list(recent_data, self.pairs)
        self.draw_info_pairs(new_values)
        self.master.after(10000, self.refresh)

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
            for pp in pairs:
                if (pair['symbol'] in pp[0]):
                    final_list.append((pair['symbol'], float(pair['price']), pp[1]))
        return final_list

    def draw_info_pairs(self, list):
        """
        Draw Tkinter window with name:price for the pairs
        :param list: a list of tuple pairs (symbol,price)
        """
        r = 2
        total_sum = 0
        eth_usd = 0
        for pair in list:
            pair_sum = pair[2] * pair[1]
            if (pair[0] == 'ETHUSDT'):
                eth_usd = float(pair[1])
            ttk.Label(self.master,
                      width=50,
                      text="Pair: {} \n Current Price: {} \n Amount: {}  \n Total: {} \n".format(pair[0], pair[1],
                                                                                                 pair[2],
                                                                                                 pair_sum),
                      font=('Courier', 12, 'bold')) \
                .grid(row=r, column=1)
            r += 1
            total_sum += pair_sum

        ttk.Label(self.master,
                  font=('Courier', 14, 'bold'),
                  width=50,
                  text="Total Value: {:.6f} in USD {:.2f}".format(total_sum, total_sum * eth_usd)) \
            .grid(row=r, column=1)


def main():
    app = CryptoViewer()


if __name__ == '__main__': main()

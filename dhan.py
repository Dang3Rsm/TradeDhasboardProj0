# 1. Fetch current holdings
# 2. Place buy order
# 3. Place sell order
# 4. Get postback from the broker
# 5. Get prices from websocket.

import pandas as pd
import os
from dhanhq import dhanhq
from dotenv import load_dotenv

class myDhan:
    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token
        self.dhan = dhanhq(self.client_id, self.access_token)
        
    def place_order(self, security_id, exchange_segment, transaction_type, quantity, order_type, product_type, price, validity=None):
        id = self.dhan.place_order(
            security_id=security_id,
            exchange_segment=exchange_segment,
            transaction_type=transaction_type,
            quantity=quantity,
            order_type=order_type,
            product_type=product_type,
            price=price,
            validity=validity
        )
        return id
        
        
    def get_order_list(self):
        return self.dhan.get_order_list()
        
    def get_order_by_id(self, order_id):
        return self.dhan.get_order_by_id(order_id)
            
    def cancel_order(self, order_id):
        self.dhan.cancel_order(order_id)
        
    def get_holdings(self):
        return self.dhan.get_holdings()

    def save_holdings_csv(self):
        try:
            holdings = self.get_holdings()
            df = pd.DataFrame(holdings)
            df.to_csv("holdings.csv", index=False)
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return -1 

    def get_security_id(self,trading_symbol,trading_exchange):
        df = pd.read_csv('api-scrip-master.csv', index_col=False, dtype='unicode')
        data = {}
        for row,i in df.iterrows():
            symbol = i['SEM_TRADING_SYMBOL']
            exchange = i['SEM_EXM_EXCH_ID']
            if symbol not in data:
                data[symbol] = {}
                data[symbol][exchange] = i.to_dict()
        return data[trading_symbol][trading_exchange]["SEM_SMST_SECURITY_ID"]


if __name__ == "__main__":
    print("--EXECUTED--")
    load_dotenv()
    CLIENT_ID = os.getenv("CLIENT_ID")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    T = myDhan(CLIENT_ID, ACCESS_TOKEN)
    T.save_holdings_csv()
    # T.place_order(security_id='52175',  #NiftyPE
    # exchange_segment=T.dhan.NSE_FNO,
    # transaction_type=T.dhan.BUY,
    # quantity=550,
    # order_type=T.dhan.MARKET,
    # product_type=T.dhan.INTRA,
    # price=0)
    #T.place_order(security_id='1333', exchange_segment=dhan.NSE, transaction_type=dhan.BUY, quantity=10, order_type=dhan.MARKET, product_type=dhan.INTRA, price=0)
    # orders =T.get_order_list()
    # print(orders)
    symbols = [
            "RELIANCE",
            "TCS",
            "HDFCBANK",
            "INFY",
            "ICICIBANK",
            "SBIN",
            "HINDUNILVR",
            "AXISBANK",
            "HDFC",
            "LT"
           ]
    #i = symbols[1]
    # for i in symbols:
    #     print(i + " " + T.get_security_id(i,"BSE"))
    print("--Killed--")

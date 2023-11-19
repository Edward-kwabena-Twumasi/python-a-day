
class BinanceWallet:

    exchange = "Binance"

    def __init__(self,name,assets = []):
        self.name = name
        self.assets = assets

    
    def __str__(self):
        return """
            Exchange : {}
            Account Name : {}
            Account Balance : {}
            Assets : {},{}
            """.format(self.exchange, self.name, 300, self.assets[0],self.assets[1])
    
    def add_asset(self,new_asset):
        self.assets.append(new_asset)
        print(f'New asset : {new_asset} .All Assets : {self.assets}')

class CryptoAsset:

    def __init__(self,name,price,quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f' {self.name} | {self.price}'
    
    def change_price(self,new_price):
        self.price = new_price




assets_raw = [("BTC",36000),("ETH",2000),("USDT",1)]

assets_data = [CryptoAsset(asset[0],asset[1]) for asset in assets_raw]

edward_wallet = BinanceWallet("Edward Kwabena Twumasi",assets_data)

print(edward_wallet)

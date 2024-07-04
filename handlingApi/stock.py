import requests

def getStock():
  url="https://api.freeapi.app/api/v1/public/stocks/stock/random"
  response=requests.get(url)
  data=response.json()

  if not data["success"]:
     raise Exception("Failed to get stock details")
  
  else:
     stock=data["data"];

  stockInfo={
     "Name":stock["Name"],
     "Symbol":["stockSymbol"],
     "ListingDate":stock["ListingDate"],
     "MarketCap":stock["MarketCap"],
     "CurrentPrice":stock["CurrentPrice"],
  }

  return stockInfo

def main():
   stock=getStock()
   print(stock)


if __name__=="__main__":
   main()


  



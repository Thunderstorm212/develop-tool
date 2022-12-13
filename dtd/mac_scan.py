import sys

from requests import get

__version__ = "1.0"


class Macpyoui:
    def __init__(self, api):
        self.api = api


site = "https://api.macvendors.com/"
data = Macpyoui(site)
macaddress = input("Please enter the MAC address: ")


def searchmac():
    macsend = data.api + macaddress
    vendorsearch = get(macsend).text
    if "Not Found" in vendorsearch:
        print("MAC address not found.")
    elif len(sys.argv) == 1:
        print("No MAC address entered.")
    else:
        print(vendorsearch)

if __name__ == "__main__":
    searchmac()
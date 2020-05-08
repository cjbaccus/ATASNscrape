#!/usr/bin/env python


from bs4 import BeautifulSoup
import re
import requests

# start loop for IP list.txt

#ata_ip = "ata2.html"


ips = [line.rstrip("\n") for line in open("iplist.txt")]

for n in ips:
    ata_ip = "http://{}/dev".format(n)
    
    htm_file = requests.get(ata_ip).text
    soup = BeautifulSoup(htm_file, 'lxml')
    pHeader = soup.find_all('p')
    #print(pHeader)

    SNpattern = "SerialNumber: (.{11})"

    match = re.search(SNpattern, str(pHeader))

    print(match[1])
          


# end loop 

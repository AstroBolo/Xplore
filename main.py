# Imports
import requests
import os
from googlesearch import search
from bs4 import BeautifulSoup

print("""
██╗░░██╗██████╗░██╗░░░░░░█████╗░██████╗░███████╗
╚██╗██╔╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝
░╚███╔╝░██████╔╝██║░░░░░██║░░██║██████╔╝█████╗░░
░██╔██╗░██╔═══╝░██║░░░░░██║░░██║██╔══██╗██╔══╝░░
██╔╝╚██╗██║░░░░░███████╗╚█████╔╝██║░░██║███████╗
╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝
""")

# Options
print("""
[1] Searh URL
[2] Search For Term
[3] Exit
""")
while True:
    main = input("[?]: ")

    if main == '1':
        a = input('Enter URL To Search: ')
        # Get Url to scrape
        r = requests.get(a)

        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')
        # Find Text In HTML
        s = soup.find('div')

        lines = soup.find_all('p')

        for line in lines:
            # Print Text
            print(line.text)

    if main == '2':
        query = input("Enter Term To Search For: ")

        # Search For Links
        for j in search(query, tld="co.in", num=20, stop=20, pause=1):
            print(j)

    if main == '3':
        # Exit Program
        break

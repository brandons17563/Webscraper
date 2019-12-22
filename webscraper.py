# Author: Brandon Schenck
# Date: 12/18/2019
# Description: Grabs html data from a specified website, organizes the data, and
# stores the data into a dataObject which is a dictionary of the parts we want
# we then add that dictionary to a python list and dump to a json file to be
# accessed by the parsedata script.

from bs4 import BeautifulSoup
import requests
import json
def main():
    # TODO: find a url to request from and parse
    url = "insert url"
    # gets html in string format
    html_code = requests.get(url).text
    # parses the html_code
    soup = BeautifulSoup(html_code,'html.parser')
    #TODO: create a loop using soup.find_all('tag',class_='class') to find info
    # block that will be put into dataObject and dumped to json file
if __name__ == "__main__":
    main()

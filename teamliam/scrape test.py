#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:32:59 2018

@author: Mikki
"""
from urllib import urlopen
url = "http://spongebob.wikia.com/wiki/Help_Wanted_(transcript)"
html = urlopen(url).read()
#html is the data but with all the html markers
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
for script in soup(["script", "style"]):
    script.extract()
print soup.prettify
raw = soup.get_text()
#raw is just the text
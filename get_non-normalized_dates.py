import csv
import lxml
from lxml import etree
import os
from os.path import join
import re


path = '/users/pjameskelly/desktop/XML_Normalized_2' # Enter the path to your EAD directory

for filename in os.listdir(path): # Loop through the files in the directory
    tree = etree.parse(join(path, filename))
    dates = tree.xpath('//unitdate') # xpath that will find a <unitdate> tag anywhere in the EAD
    undated = re.compile('^[Uu](ndated)$') # Regular expression to match 'undated' or 'Undated'
    for date in dates:
        if date.text and not undated.match(date.text) and not 'normal' in date.attrib: # Check if the text of the date matched 'undated' and if the date has an normal attribute
            with open('non-normalized_dates.csv', 'ab') as csvfile: # Open a csv for writing our output
                writer = csv.writer(csvfile, dialect='excel')
                writer.writerow([filename, tree.getpath(date), date.text.encode('utf-8')]) # Write the filename, xpath to the date, and text of the date to the csv
    print filename

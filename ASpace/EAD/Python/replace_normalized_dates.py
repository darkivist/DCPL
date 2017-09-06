# import what we need
import csv
from lxml import etree
from os.path import join

path = '/users/pjameskelly/desktop/XML_Normalized' # Enter the path to your EAD directory here

normalized_file = '/users/pjameskelly/desktop/remainders.csv' # Enter the path to the exported CSV here

with open(normalized_file, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None) # Skip the header row
    for row in reader: # Loop through the rows in the csv
        filename = row[0]
        date_path = row[1]
        # uncomment the line below if you also cleaned up the date expression
        #expression = row[3]
        normalized = row[4]
        ead = open(join(path, filename)) # Open the EAD
        tree = etree.parse(ead)
        date = tree.xpath(date_path)
        # uncomment the line below if you also cleaned up the date expression
        #date[0].text = expression
        date[0].attrib['normal'] = normalized # Add a normal attribute with the normalized date
        outfile = open(join(path, filename), 'w')
        outfile.write(etree.tostring(tree, encoding="utf-8", xml_declaration=True)) # Rewrite the EAD to save the normalization
        outfile.close()

print "Normalization complete" # Woo!

# Get ISO metadata from CSV file

import pandas as pd
import urllib.request

def main():
    
    df = pd.read_csv("../data/erddap_iso.csv", sep="\n")
    iso_list = []
    url_list = list(df[df.columns[0]])
    
    for iso_url in url_list:
        response = urllib.request.urlopen(iso_url).read().decode()
        iso_list.append(response)

    #print(response)
    
    # Create a file to hold ISO XML
    fo = open("./output/erddap_iso_combined.xml", "x")
    
    fo.write("<?xml version = '1.0' encoding='UTF-8'?>")
    
    fo.write("<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>" )

    for entry in iso_list:
        fo.write("<rdf:Description>")
        fo.write(str(entry))
        fo.write("</rdf:Description \n")
        
    fo.write("</rdf:RDF>")
    
    fo.close()
        
main()

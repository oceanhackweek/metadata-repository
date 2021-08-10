# Convert ISO XML to RDF XML
import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml

def get_file_id(soup):
    file_character_string = soup.find("gmd:fileIdentifier")
    file_id_text = file_character_string.text

    return(file_id_text)

def get_abstract(soup):
    abstract_character_string = soup.find("gmd:abstract")
    abstract_text = abstract_character_string.text

    return(abstract_text)

def get_keywords(soup):
    keywords_list = []
    
    keywords_character_string = soup.find_all("gmd:keyword")
    
    for word in keywords_character_string:
        keywords_list.append(word.text)
        
    return((keywords_list))


def main():

    #'''
    df = pd.read_csv("../data/erddap_iso.csv")
    url_list = list(df[df.columns[0]])

    # Attribute lists
    file_id_list = []
    abstract_list = []
    keywords_list = []

    for iso_url in url_list:
        page = requests.get(iso_url)

        soup = BeautifulSoup(page.text, "xml")

        file_id_list.append(get_file_id(soup))
        abstract_list.append(get_abstract(soup))
        
        #Keywords
        keywords_string = get_keywords(soup)
        #keywords_split = list(keywords_string.split(","))
        keywords_list.append(keywords_string)
    
    iso_dict = {"id": file_id_list,
                "abstract": abstract_list,
                "keywords": keywords_list
                }
    print(iso_dict["keywords"])
    print(type(iso_dict["keywords"]))
    #test
    #exit()
    iso_df = pd.DataFrame(iso_dict)
    print(type(iso_df["keywords"]))
    print(iso_df["keywords"])
    print(type(iso_df["keywords"][0]))
    
    iso_df.to_csv("./output/iso_extract.csv")
    #'''
    # Test
    #print(file_id_list)
    #print(iso_df)
    
    #If iso_extract.csv" already exists, load it
    #iso_df = pd.read_csv("iso_extract.csv")
    
    # Build RDF
    fo = open("./output/iso_rdf.xml", "w")

    fo.write("<?xml version = '1.0' encoding='UTF-8'?>")
    
    fo.write("<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' xmlns:dc='http://purl.org/dc/elements/1.1/' xmlns:dct='http://purl.org/dc/terms/'>")
             
    for row in iso_df.index:
        fo.write("<rdf:Description>")
        id_string = "<dc:identifier>" + iso_df['id'][row] + "</dc:identifier>"
        abstract_string = "<dct:abstract>" + iso_df['abstract'][row] + "</dct:abstract>"
             
        fo.write(id_string)
        
        keywords_string_list = list(iso_df['keywords'][row])
        for word in keywords_string_list:
            word = word.strip("\n")
            keyword_string = "<dc:subject>" + str(word) + "</dc:subject>"
            fo.write(keyword_string)
             
        fo.write(abstract_string)
        fo.write("</rdf:Description> \n")
                                                   
    fo.write("</rdf:RDF>")  
        
    fo.close()
main()

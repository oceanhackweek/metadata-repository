from requests.api import request
import requests
import xml.dom.minidom
import datetime
import pandas as pd

def get_irish_meta_as_xml(id, file = "Archive_Irish_marine_fish_data.xml"):
  ## create the base url to get the data given an unique ID

  ## id: unique ID for any dataset in the Irish Marine data center
  ## file: file to save xml to local machine

  base_url = "http://data.marine.ie/geonetwork/srv/api/records/ie.marine.data:dataset." + str(id) + "/formatters/xml"

  ## create a request 
  response_irish = requests.get(url=base_url, timeout=120.00)

  ## send http request to center 
  if response_irish.status_code != 200:
    sendmail(base_url)

  ## if request is successful, write xml to file in disk
  if response_irish.status_code == 200:
    with open(file, "wb") as f:
      f.write(response_irish.content)

## test function    
get_irish_meta_as_xml(982, file = "CE16007.xml")

def parse_xml(docfile):
  ## parse xml file to useful data structure we can use in python 

  ## create a DOM list 
  doc = xml.dom.minidom.parse(docfile)

  ## use the custom tree layout of the xml to get individual field (eg contact address, contact, abstract, bounding box)

  ## get the organisation name as string nested in contact
  fileid = doc.getElementsByTagName("gmd:contact")
  fileid = fileid[0].getElementsByTagName('gmd:organisationName')[0].getElementsByTagName('gco:CharacterString')[0]
  institute = fileid.childNodes[0].data

  ## get the title of project as string
  fileid = doc.getElementsByTagName("gmd:title")[0].getElementsByTagName('gco:CharacterString')[0]
  title = fileid.childNodes[0].data

  ## get the abstract of project as string
  fileid = doc.getElementsByTagName("gmd:abstract")[0]
  abstract = fileid.getElementsByTagName("gco:CharacterString")[0].childNodes[0].data

  ## get the data email responsible for project nested in contactinfo, nested in CI_responsibleParty
  fileid = doc.getElementsByTagName("gmd:CI_ResponsibleParty")[0].getElementsByTagName("gmd:contactInfo")[0]
  email = fileid.getElementsByTagName("gmd:electronicMailAddress")[0].getElementsByTagName("gco:CharacterString")[0].childNodes[0].data
  
  ## get the bounding box where the sample was taken
  fileid = doc.getElementsByTagName("gmd:EX_GeographicBoundingBox")[0].childNodes
  lonwest = doc.getElementsByTagName("gmd:westBoundLongitude")[0].getElementsByTagName("gco:Decimal")[0].childNodes[0].data
  loneast = doc.getElementsByTagName("gmd:eastBoundLongitude")[0].getElementsByTagName("gco:Decimal")[0].childNodes[0].data
  latsouth = doc.getElementsByTagName("gmd:southBoundLatitude")[0].getElementsByTagName("gco:Decimal")[0].childNodes[0].data
  latnorth = doc.getElementsByTagName("gmd:northBoundLatitude")[0].getElementsByTagName("gco:Decimal")[0].childNodes[0].data

  ## put all result into a Dictionary
  result = {}
  result["institute"] = institute
  result["title"] = title
  result["abstract"] = abstract
  result["email"] = email
  result["bounding_box"] = [lonwest, loneast, latsouth, latnorth]

  return result

irish_marine_metadata_result = parse_xml("CE16007.xml")
irish_fish_metadata_result = parse_xml("Archive_Irish_marine_fish_data.xml")

print(irish_marine_metadata_result)


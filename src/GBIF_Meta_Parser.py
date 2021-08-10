
def get_GBIF_data(url, write=False, file = None):
    # create request
  response_pcr = requests.get(url=url, timeout=120.00)
  
  ## check defensive for error
  if response_pcr.status_code != 200:
    sendmail(url)
  
  ## return content or write to file
  if not write:
    return response_pcr.content
  else:
    if response_pcr.status_code == 200:
      with open(file, "wb") as f:
        f.write(response_pcr.content)

## test function
pcr_url = "https://www.dassh.ac.uk/ipt/eml.do?r=pacific-cpr-phyto&v=1.2"

docfile = get_GBIF_data(pcr_url, write=False)
# docfile = get_GBIF_data(pcr_url, write=False, file="PCR_Pacific_CPR_Survey.xml")

def coordinate_PCR(doc, coord):
    # helper function to deal with coordinate bounding box
  return doc.getElementsByTagName(coord)[0].childNodes[0].data


def Plankton_PCR_GBIF(docfile):
    ## test to see which input file we have 
  if type(docfile) is str:
    doc_tmp = xml.dom.minidom.parse(docfile)
  else:
    doc_tmp = xml.dom.minidom.parseString(docfile)

    ## get title
  title = doc_tmp.getElementsByTagName("title")[0].childNodes[0].data

    ## get organisation
  organisation = doc_tmp.getElementsByTagName("organizationName")[0].childNodes[0].data
  ## get email
  email = doc_tmp.getElementsByTagName("electronicMailAddress")[0].childNodes[0].data 
  ## get abstract
  abstract = doc_tmp.getElementsByTagName("abstract")[0].childNodes[1].childNodes[0].data
 ## get bounding box
  coords = ["westBoundingCoordinate", "eastBoundingCoordinate", "northBoundingCoordinate", "southBoundingCoordinate"]
  LineString = []
  for coord in coords:
      try:
          LineString.append(coordinate_PCR(doc_tmp, coord))
      except IndexError:
        LineString.append(999)

    ## get date range 
  range_date = []
  for date in doc_tmp.getElementsByTagName("calendarDate"):
    range_date.append(date.childNodes[0].data)
  
  ## get citation    
  if len(doc_tmp.getElementsByTagName("citation")) >= 1:
      try:
          Bib = doc_tmp.getElementsByTagName("citation")[1].childNodes[0].data
      except:
          Bib = doc_tmp.getElementsByTagName("citation")[0].childNodes[0].data
  else:
      Bib = doc_tmp.getElementsByTagName("citation")

          

    ## store all in result vector
  results = {}
  results["title"] = title
  results["organisation"] = organisation
  results["email"] = email
  results["abstract"] = abstract
  results["Bounding_box"] = LineString
  results["Citation"] = Bib

    ## return 
  return results  

## test function 
Plankton_PCR_GBIF(docfile)

## other file in the GBIF Website can also be retrieved through this 
# eg: https://www.dassh.ac.uk/ipt/resource?r=pacific-cpr-phyto#project

zooplankton_Skinner_Solway = get_GBIF_data(url = "https://www.dassh.ac.uk/ipt/eml.do?r=dasshse00000035&v=2.1", write=False)
Plankton_PCR_GBIF(zooplankton_Skinner_Solway)
docfile = zooplankton_Skinner_Solway

# base_url = "https://www.dassh.ac.uk/ipt/"
# projectid = "dasshdt00000144" 
# xml_page = base_url + "eml.do?r=" + projectid + "&v=2.1"

barnacle = get_GBIF_data(url="https://www.dassh.ac.uk/ipt/eml.do?r=dasshdt00000144&v=1.5", write=False)
Plankton_PCR_GBIF(barnacle)

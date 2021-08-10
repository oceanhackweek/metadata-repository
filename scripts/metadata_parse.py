# Metadata parsing
# Description:

import kglab
import pandas as pd

def main():
    
    # Load emodnet data into knowledge graph (kg)
    kg = kglab.KnowledgeGraph().load_rdf("../data/emodnet_metadata.xml", format="xml")
    
    #Load erddap data into kg
    kg.load_rdf("../data/iso_rdf.xml", format="xml")
    
    VIS_STYLE = {
    "_": {
        "color": "orange",
        "size": 40
    },
    "iso": {"color": "red",
           "size": 40}
        
}


    subgraph = kglab.SubgraphTensor(kg)
    pyvis_graph = subgraph.build_pyvis_graph(style = VIS_STYLE)

    pyvis_graph.force_atlas_2based()
    pyvis_graph.show("./output/tmp.metadata.html")
    
    # SPARQL Query
    sparql = """
SELECT ?dataset ?title ?id
  WHERE {
      ?dataset dc:type dc:dataset .
      ?dataset dc:title ?title .
      ?dataset dc:identifier ?id .
  }
  
  """
    
    #df = kg.query_as_df(sparql)
    
    #df.to_csv("emodnet_dataset_id.csv")
    
    

main()



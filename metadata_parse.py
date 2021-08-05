# Metadata parsing
# Description:

import kglab
import pandas as pd

def main():

    kg = kglab.KnowledgeGraph().load_rdf("emodnet_metadata.xml", format="xml")

    #subgraph = kglab.SubgraphTensor(kg)
    #pyvis_graph = subgraph.build_pyvis_graph()

    #pyvis_graph.force_atlas_2based()
    #pyvis_graph.show("tmp.fig03.html")
    
    # SPARQL Query
    sparql = """
SELECT ?dataset ?title
  WHERE {
      ?dataset dc:type dc:dataset .
      ?dataset dc:title ?title .
  }
  LIMIT 10
  """
    
    #df = kg.query_as_df(sparql)
    
    #print(df)

main()



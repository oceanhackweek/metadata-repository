# Metadata parsing
# Description:

from owslib.csw import CatalogueServiceWeb
import kglab

def main():

    #csw = CatalogueServiceWeb("https://emodnet.ec.europa.eu/geonetwork/emodnet/eng/csw?service=CSW&request=GetCapabilities&VERSION=2.0.2")
    #print(csw.identification.type)
    
    kg = kglab.KnowledgeGraph().load_rdf("emodnet_metadata.xml", format="xml")
    
    
    subgraph = kglab.SubgraphTensor(kg)
    pyvis_graph = subgraph.build_pyvis_graph()
    
    pyvis_graph.force_atlas_2based()
    pyvis_graph.show("tmp.fig03.html")

main()
    
    

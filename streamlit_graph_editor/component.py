import streamlit.components.v1 as components
import networkx as nx
import os

# Declare the custom component
component_name = "graph_editor_component"
component_path = os.path.join(os.path.dirname(__file__), 'frontend')

_graph_editor = components.declare_component(
    component_name,
    path=component_path
)

def graph_editor(graph_data, actions, treeMode, node_attribute_keys, title, key):
    '''
    Friendly function that will serve our component
    '''    
    edited_graph = _graph_editor(
                        graph_data=graph_data, 
                        actions=actions,
                        treeMode=treeMode,
                        node_attribute_keys=node_attribute_keys,
                        graph_title=title,
                        key=key
                    )
    if edited_graph:
        return edited_graph
    return graph_data

# 🔹 Helper function: Convert `networkx.Graph` to JSON format for `vis-network`
def from_networkx(graph: nx.DiGraph):
    nodes = [{"id": str(n), "label": str(n), "attributes": graph.nodes[n] } for n in graph.nodes()]
    edges = [{"from": str(u), "to": str(v)} for u, v in graph.edges()]
    return {"nodes": nodes, "edges": edges}

# 🔹 Helper function: Convert JSON output from Streamlit component back to `networkx.Graph`
def to_networkx(graph_data):
    G = nx.DiGraph()
    for node in graph_data["nodes"]:
        G.add_node(node["id"], **(node.get("attributes") or {}))
    for edge in graph_data["edges"]:
        G.add_edge(edge["from"], edge["to"])
    return G

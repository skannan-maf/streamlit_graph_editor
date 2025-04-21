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

def graph_editor(
        graph_data,
        tree_mode,
        is_directed,
        node_attribute_keys,
        edge_attribute_keys,
        title,
        key
    ):
    '''
    A friendly function that will serve the graph editor component
    
    ARGUMENTS
    graph_data: Graph structure in JSON format
        Example:
        {
            "nodes": [{"id": someid, "label": "somelabel", "attributes": {key: value, ...}}, ..... ], 
            "edges": [{"from": "from_id", "to":"to_id"},...]
        }
    tree_mode: If true, then the editor will enforce "tree" semantics while editing the graph. Otherwise not. 
    is_directed: If true, then the editor will render the graph as a Directed graph 
    node_attribute_keys: A list of keys to be used as node attributes
                         When user selects to edit node attributes, the editor will input the values for the 
                         keys specified here
    title: Title of the graph 
    key: Widget key so that multiple instances of graph editors do not clash
    '''
    edited_graph = _graph_editor(
                        graphData=graph_data,
                        treeMode=tree_mode,
                        isDirected=is_directed,
                        nodeAttributeKeys=node_attribute_keys,
                        edgeAttributeKeys=edge_attribute_keys,
                        graphTitle=title,
                        key=key
                    )
    if edited_graph:
        return edited_graph
    return graph_data

# 🔹 Helper function: Convert `networkx.Graph` to JSON format for `vis-network`
def from_networkx(graph: nx.DiGraph):
    nodes = [{"id": str(n), "label": str(n), "attributes": graph.nodes[n] } for n in graph.nodes()]
    edges = [{"from": str(u), "to": str(v), "attributes": graph.edges[u, v]} for u, v in graph.edges()]
    return {"nodes": nodes, "edges": edges}

# 🔹 Helper function: Convert JSON output from Streamlit component back to `networkx.Graph`
def to_networkx(graph_data):
    G = nx.DiGraph()
    for node in graph_data["nodes"]:
        G.add_node(node["id"], **(node.get("attributes") or {}))
    for edge in graph_data["edges"]:
        G.add_edge(edge["from"], edge["to"], **(edge.get("attributes") or {}))
    return G

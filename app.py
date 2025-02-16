import streamlit as st
import networkx as nx
from streamlit_graph_editor import graph_editor 

st.set_page_config(layout="wide")

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

# 🔹 Define an example graph using `networkx`
G = nx.DiGraph()  # Use `nx.Graph()` for an undirected graph
G.add_edges_from([
    ("1", "2"),
    ("1", "3"),
    ("2", "4"),
])

# Convert the `networkx` graph to JSON format
initial_graph = from_networkx(G)

# Define allowed node attribute keys
node_attribute_keys = ["Owner", "Email", "Department"]  # ✅ Specify keys

# Allowed user actions
allowed_actions = {
    "add_node": True,
    "add_child_node": True,
    "add_edge": True,
    "delete_edge": True,
    "delete_node": True,
    "delete_subtree": True,
    "add_node_attribute": True,
    "delete_node_attribute": True
}

user_graph = graph_editor(
                graph_data=initial_graph, 
                actions=allowed_actions, 
                treeMode=True, 
                node_attribute_keys=node_attribute_keys,
                title="The origin of time", 
                key="graph_editor"
            )

# Display results
st.subheader("User-Edited Graph Output:")
if user_graph:
    st.json(user_graph)
    edited_graph = to_networkx(user_graph)
    st.subheader("Re-loaded as NetworkX Graph")
    st.write(edited_graph.edges)

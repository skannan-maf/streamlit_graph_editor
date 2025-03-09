import streamlit as st
import networkx as nx
from streamlit_graph_editor import graph_editor, from_networkx, to_networkx

st.set_page_config(layout="wide")

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

user_graph = graph_editor(
                graph_data=initial_graph,
                tree_mode=True, 
                is_directed=False,
                node_attribute_keys=node_attribute_keys,
                title="Origin",
                key="graph_editor"
            )

# Display results
st.subheader("User-Edited Graph Output:")
if user_graph:
    st.json(user_graph)
    edited_graph = to_networkx(user_graph)
    st.subheader("Re-loaded as NetworkX Graph")
    st.write(':blue[Edge list]')
    st.write(edited_graph.edges)

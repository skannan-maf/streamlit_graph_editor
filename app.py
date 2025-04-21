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

# Create node attributes
G.nodes['1'].update({'Name': 'Number 1', 'Owner': 'Main', 'Email': 'a@a.com'})
G.nodes['2'].update({'Name': 'Number 2', 'Owner': 'Train'})

# Create edge attributes
G.edges['1', '2']['Weight'] = 5
G.edges['1', '2']['Type'] = 'Type A'

# Convert the `networkx` graph to JSON format
initial_graph = from_networkx(G)

# Define allowed node attribute keys
node_attribute_keys = ["Name", "Owner", "Email", "Department"]  # ✅ Specify keys
edge_attribute_keys = ["Weight", "Type"]  # ✅ Specify keys

user_graph = graph_editor(
                graph_data=initial_graph,
                tree_mode=True, 
                is_directed=False,
                node_attribute_keys=node_attribute_keys,
                edge_attribute_keys=edge_attribute_keys,
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
    for edge in edited_graph.edges:
        st.write('Attributes for edge {} = {}'.format(edge, edited_graph.edges[edge]))
    
    st.write(':blue[Node list]')
    st.write(edited_graph.nodes)
    for node in edited_graph.nodes:
        st.write('Attributes for node {} = {}'.format(node, edited_graph.nodes[node]))

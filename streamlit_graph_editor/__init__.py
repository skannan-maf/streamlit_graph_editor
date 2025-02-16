import streamlit.components.v1 as components
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
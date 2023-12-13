import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
graph = nx.DiGraph()

# Define nodes for the graph
nodes = [
    "Process A", "Process B", "Message Queue",
    "System Call Interface", "Scheduler", "Interrupt Handler"
]
graph.add_nodes_from(nodes)

# Define edges (relationships) for the graph
edges = [
    ("Process A", "System Call Interface", {"label": "send"}),
    ("System Call Interface", "Message Queue", {"label": "enqueue message"}),
    ("Message Queue", "System Call Interface", {"label": "message ready"}),
    ("System Call Interface", "Process B", {"label": "receive"}),
    ("Process A", "Scheduler", {"label": "request schedule"}),
    ("Scheduler", "Process A", {"label": "schedule"}),
    ("Interrupt Handler", "Process A", {"label": "interrupt"}),
    ("Process A", "Interrupt Handler", {"label": "handle"})
]
graph.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(graph)  # Node positions
nx.draw(graph, pos, with_labels=True, arrows=True,
        node_size=3000, node_color='skyblue', font_size=10)

# Add edge labels
edge_labels = nx.get_edge_attributes(graph, "label")
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

# Text descriptions in English
text_descriptions = [
    "Processor State Transitions:\nDuring system calls, the processor switches from user mode to kernel mode.\nThe scheduler may change the process state (e.g., from running to waiting).",
    "Information Flow:\nFrom process to message queue (sending message).\nFrom message queue to another process (receiving message).\nIn case of an interrupt, from the interrupt handler to the process."
]
plt.figtext(0.5, -0.1, "\n\n".join(text_descriptions), ha="center",
            fontsize=10, bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5})

plt.title("IPC Implementation Framework Based on proc.h and proc.c")
plt.axis('off')
plt.show()

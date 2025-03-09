#!/usr/bin/python

# AI_ML_3D_CLayers.py - 3D Visualization of AI/ML Ecosystem Conceptual Layers 
# A python program utilizing plotly for 3D Visualization of AI/ML Ecosystem Conceptual Layers.
# Copyright (C) 2025 M. B. Ghaznavi-Ghoushchi
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.


import networkx as nx
import plotly.graph_objects as go
import numpy as np
import math

G = nx.DiGraph()
core_hws = ["Nvidia", "Cerebras", "TSMC", "Intel", "AMD"]
for hw in core_hws:
    G.add_node(hw, level=0, description=f"{hw}: Core hardware provider.")  
core_llms = ["ChatGPT", "Deepseek", "Grok", "Gemini", "Qwen"]
for llm in core_llms:
    G.add_node(llm, level=1, description=f"{llm}: Core large language model.")  
    for hw in core_hws:
        G.add_edge(hw, llm)
agent_tools = [
    "pdf.ai", "pandas-ai", "perplexity.ai", "openrouter.ai", "notebooklm.google.com",
    "Carl from AutoScience", "Gitingest", "Review-it.me", "Observe.ai", "CallMiner", "ExecVision"
]
for tool in agent_tools:
    G.add_node(tool, level=2, description=f"{tool}: Agent-based tool.")  
    for llm in core_llms:
        G.add_edge(llm, tool)
domain_specific_tools = [
    "Semikong", "GeoSpy", "Med-PaLM", "Genesis", "Canvasxpress", "Litmaps", "PathAI", "BloombergGPT"
]
for domain in domain_specific_tools:
    G.add_node(domain, level=3, description=f"{domain}: Domain-specific AI tool.")  
    for agent_tool in agent_tools:
        G.add_edge(agent_tool, domain)
humans = ["Human", "Smart Humanoid"]
for human in humans:
    G.add_node(human, level=4, description=f"{human}: Human/humanoid layer.")  
    for domain in domain_specific_tools:
        G.add_edge(domain, human)
for tool in domain_specific_tools:
    for agent_tool in agent_tools:
        G.add_edge(tool, agent_tool)
    for llm in core_llms:
        G.add_edge(tool, llm)
for agent_tool in agent_tools:
    for llm in core_llms:
        G.add_edge(agent_tool, llm)
for hw in core_hws:
    if hw == "Nvidia":
        G.nodes[hw]["description"] = f"<b>{hw}</b>: Core HW service.<br>"
    elif hw == "Cerebras":
        G.nodes[hw]["description"] = f"<b>{hw}</b>: Core HW service.<br>"
    elif hw == "TSMC":
        G.nodes[hw]["description"] = f"<b>{hw}</b>: Core HW service.<br>"
for llm in core_llms:
    if llm == "ChatGPT":
        G.nodes[llm]["description"] = f"<b>{llm}</b>: Core LLM service.<br>"
    elif llm == "Deepseek":
        G.nodes[llm]["description"] = f"<b>{llm}</b>: Core LLM service.<br>"
    elif llm == "Grok":
        G.nodes[llm]["description"] = f"<b>{llm}</b>: Core LLM service.<br>"
    elif llm == "Gemini":
        G.nodes[llm]["description"] = f"<b>{llm}</b>: Core LLM service.<br> (Google DeepMind)"
    elif llm == "Qewin":
        G.nodes[llm]["description"] = f"<b>{llm}</b>: Core LLM service.<br>"
    elif llm == "BloombergGPT":
        G.nodes[llm]["description"] = f"<b>{llm}</b>: Core LLM service.<br> (Bloomberg proprietary model)"
for tool in agent_tools:
    if tool == "pdf.ai":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "pandas-ai":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "perplexity.ai":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "openrouter.ai":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "notebooklm.google.com":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "Carl from AutoScience":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "Gitingest":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "Review-it.me":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "Observe.ai":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "CallMiner":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
    elif tool == "ExecVision":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Agent-based tool.<br>"
for tool in domain_specific_tools:
    if tool == "Semikong":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Domain-specific AI tool.<br>"
    elif tool == "GeoSpy":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Domain-specific AI tool.<br>"
    elif tool == "Med-PaLM 2":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Domain-specific AI tool.<br> (Google Medical AI)"
    elif tool == "Genesis":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Domain-specific AI tool.<br>"
    elif tool == "Canvasxpress.org":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Domain-specific AI visualization platform.<br>"
    elif tool == "Litmaps.com":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Domain-specific literature mapping platform.<br>"
    elif tool == "PathAI":
        G.nodes[tool]["description"] = f"<b>{tool}</b>: Medical diagnostics AI platform.<br>"
for human in humans:
    if human == "Human":
        G.nodes[human]["description"] = f"<b>{human}</b>: End user accessing all layers.<br>"
    elif human == "Smart Humanoid":
        G.nodes[human]["description"] = f"<b>{human}</b>: End user-alike accessing all layers.<br>"

levels = {
    0: -2.5,
    1: -1.5,
    2: -0.5,
    3: 0.5,
    4: 1.5
}
nodes_by_level = {level: [] for level in levels}
for node in G.nodes():
    level = G.nodes[node]['level']
    nodes_by_level[level].append(node)
pos = {}
for level, nodes in nodes_by_level.items():
    num_nodes = len(nodes)
    radius = 1.0  
    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / num_nodes
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = levels[level]
        pos[node] = (x, y, z)
x_nodes = [pos[node][0] for node in G.nodes()]
y_nodes = [pos[node][1] for node in G.nodes()]
z_nodes = [pos[node][2] for node in G.nodes()]
descriptions = [G.nodes[node]["description"] for node in G.nodes()]
edge_x = []
edge_y = []
edge_z = []
for edge in G.edges():
    x0, y0, z0 = pos[edge[0]]
    x1, y1, z1 = pos[edge[1]]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]
    edge_z += [z0, z1, None]
edge_trace = go.Scatter3d(
    x=edge_x,
    y=edge_y,
    z=edge_z,
    mode='lines',
    line=dict(color='lightgray', width=2),
    hoverinfo='none'
)
node_trace = go.Scatter3d(
    x=x_nodes,
    y=y_nodes,
    z=z_nodes,
    mode='markers+text',
    marker=dict(
        size=15,
        color=[G.nodes[node]['level'] for node in G.nodes()],  
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(title='')
    ),
    text=list(G.nodes()),
    textposition="top center",
    hoverinfo='text',
    hovertemplate='%{customdata}<extra></extra>',  
    customdata=[G.nodes[node]["description"] for node in G.nodes()]  
)
x_plane = np.linspace(-1.5, 1.5, 100)
y_plane = np.linspace(-1.5, 1.5, 100)
X, Y = np.meshgrid(x_plane, y_plane)
z_values = [-2.5, -1.5, -0.5, 0.5, 1.5]  
plane_traces = []
colorscales = ['Blues', 'Reds', 'Greens', 'Oranges', 'Reds']  
for i, z in enumerate(z_values):
    Z = np.full_like(X, z)
    plane_trace = go.Surface(
        x=X,
        y=Y,
        z=Z,
        opacity=0.2,
        showscale=False,
        colorscale=colorscales[i],
        hoverinfo='none'
    )
    plane_traces.append(plane_trace)
annotations = [
    dict(
        showarrow=False,
        x=-1.4,  
        y=-1.5,
        z=z_values[0],
        text="Core HWs",
        xanchor="center",
        yanchor="middle",
        font=dict(size=20),
        textangle=0
    ),
    dict(
        showarrow=False,
        x=-1.4,  
        y=-1.5,
        z=z_values[1],
        text="Core LLMs",
        xanchor="center",
        yanchor="middle",
        font=dict(size=20),
        textangle=0
    ),
    dict(
        showarrow=False,
        x=-1.4,  
        y=-1.5,
        z=z_values[2],
        text="Agent-Based Tools",
        xanchor="center",
        yanchor="middle",
        font=dict(size=20),
        textangle=0
    ),
    dict(
        showarrow=False,
        x=-1.4,  
        y=-1.5,
        z=z_values[3],
        text="Domain-Specific Tools",
        xanchor="center",
        yanchor="middle",
        font=dict(size=20),
        textangle=0
    ),
    dict(
        showarrow=False,
        x=-1.4,  
        y=-1.5,
        z=z_values[4],
        text="Humans",
        xanchor="center",
        yanchor="middle",
        font=dict(size=20),
        textangle=0
    )
]
fig = go.Figure(data=[edge_trace, node_trace] + plane_traces)
fig.update_layout(
    title=dict(text="3D Visualization of AI/ML Ecosystem Conceptual Layers", font=dict(size=24), x=0.5),
    scene=dict(
        xaxis=dict(
            title=dict(text="X-Axis", font=dict(size=15)),
            tickfont=dict(size=12)  
        ),
        yaxis=dict(
            title=dict(text="Y-Axis", font=dict(size=15)),
            tickfont=dict(size=12)  
        ),
        zaxis=dict(
            title=dict(text="Layer Level", font=dict(size=15)),
            tickfont=dict(size=12)  
        ),
        annotations=annotations
    ),
)
fig.show()

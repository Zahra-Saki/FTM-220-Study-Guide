import json
from shiny import App, render, ui

# Complete mind map hierarchy transcribed from your study guide
mindmap_data = {
    "name": "Fashion Supply Chain Management Study Guide",
    "children": [
        {
            "name": "Fundamentals of SCM",
            "children": [
                {
                    "name": "Working Definition",
                    "children": [
                        {"name": "Collaboration of Stakeholders"},
                        {"name": "Seamless Production and Delivery"},
                    ],
                },
                {
                    "name": "Essential Operations",
                    "children": [
                        {"name": "Sourcing and Procurement"},
                        {"name": "Production and Logistics"},
                        {"name": "Inventory Management"},
                        {"name": "Supply Network Control"},
                    ],
                },
                {
                    "name": "Industry Lifeline",
                    "children": [
                        {"name": "Economic Movement"},
                        {"name": "Overall Efficiency"},
                        {"name": "Customer Expectations"},
                    ],
                },
            ],
        },
        {
            "name": "Historical Development",
            "children": [
                {
                    "name": "Industrial Revolution",
                    "children": [
                        {"name": "Innovations in Textile Mills"},
                        {"name": "Evolution of Transportation"},
                        {"name": "Advancements in Logistics"},
                    ],
                },
                {
                    "name": "Commercial Development",
                    "children": [
                        {"name": "Standardized Size Systems"},
                        {"name": "World Assembly Line Concept"},
                        {"name": "Mass Market Production"},
                    ],
                },
                {
                    "name": "Technology and Modern Era",
                    "children": [
                        {"name": "Fast Fashion Evolution"},
                        {"name": "Barcoding and UPC Systems"},
                        {"name": "Electronic Data Interchange (EDI)"},
                        {"name": "Material Requirements Planning (MRP)"},
                    ],
                },
                {
                    "name": "Modern Market",
                    "children": [
                        {"name": "Global Production Networks"},
                        {"name": "Sourcing and Logistics Integrations"},
                        {"name": "Fast Fashion Expansion"},
                    ],
                },
            ],
        },
        {
            "name": "The Global Supply Chain",
            "children": [
                {
                    "name": "Framework and Scope",
                    "children": [
                        {"name": "Global Footprint Networks"},
                        {"name": "Material Sourcing"},
                        {"name": "Interconnected Services"},
                    ],
                },
                {
                    "name": "Governments and Trade Policy",
                    "children": [
                        {"name": "Tariffs and Quotas"},
                        {"name": "Mass Sourcing Arrangements"},
                        {"name": "WTO Framework Impact"},
                        {"name": "Trade Agreements and Tariffs"},
                    ],
                },
                {
                    "name": "Sourcing Options",
                    "children": [
                        {"name": "Global Sourcing Networks"},
                        {"name": "Nearshoring and Reshoring"},
                        {"name": "Onshoring / Domestic Sourcing"},
                        {"name": "Outsourcing vs In-house Sourcing"},
                    ],
                },
                {
                    "name": "Logistics Infrastructure",
                    "children": [
                        {"name": "Multimodal Infrastructure"},
                        {"name": "Distribution and Supply Chains"},
                        {"name": "Hub Strategies"},
                    ],
                },
            ],
        },
        {
            "name": "Corporate Social Responsibility",
            "children": [
                {
                    "name": "CSR and Sustainability Concepts",
                    "children": [
                        {"name": "Environmental Impact Concerns"},
                        {"name": "Resource Footprint Audits"},
                    ],
                },
                {
                    "name": "Metrics and Actions",
                    "children": [
                        {"name": "Sustainable Materials"},
                        {"name": "Water and Energy Sparing Processes"},
                        {"name": "Waste Reduction Strategies"},
                    ],
                },
                {
                    "name": "Ethical Challenges",
                    "children": [
                        {"name": "Human Rights and Fair Wages"},
                        {"name": "Unsafe Working Conditions"},
                        {"name": "Pollution/Waste and Landfills"},
                    ],
                },
                {
                    "name": "Key Strategic Participants",
                    "children": [
                        {"name": "Brands and Designers"},
                        {"name": "Primary Supply Chain (CMT/FOB)"},
                        {"name": "Third-Party Collaborators"},
                    ],
                },
            ],
        },
        {
            "name": "Modern Market Disruptors",
            "children": [
                {
                    "name": "Commercial Expectations",
                    "children": [
                        {"name": "Shifting Consumer Demands"},
                        {"name": "Autonomy and Eco-conscious Designs"},
                    ],
                },
                {
                    "name": "Pressure of Social Media",
                    "children": [
                        {"name": "Real-Time Feedback Loops"},
                        {"name": "Micro-Trends and Influencers"},
                    ],
                },
                {
                    "name": "Ecommerce Pressure",
                    "children": [
                        {"name": "Omnichannel Distribution"},
                        {"name": "Operational Infrastructure"},
                        {"name": "Direct-to-Consumer Models"},
                    ],
                },
            ],
        },
    ],
}


def build_horizontal_mindmap_html(data):
    data_json = json.dumps(data)
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: system-ui, -apple-system, sans-serif;
            background: #ffffff;
            overflow: hidden;
            user-select: none;
        }}
        #mindmap-container {{
            width: 100vw;
            height: 100vh;
            cursor: grab;
        }}
        #mindmap-container:active {{
            cursor: grabbing;
        }}
        .link {{
            fill: none;
            stroke: #94a3b8;
            stroke-width: 1.5px;
        }}
        .node {{
            cursor: pointer;
        }}
        .node text {{
            font-size: 12px;
            font-weight: 500;
            fill: #0f172a;
            text-anchor: middle;
            dominant-baseline: central;
            pointer-events: none;
        }}
        .toggle-btn circle {{
            fill: #64748b;
            stroke: #ffffff;
            stroke-width: 1px;
        }}
        .toggle-btn text {{
            fill: #ffffff;
            font-size: 10px;
            font-weight: bold;
            pointer-events: none;
            text-anchor: middle;
            dominant-baseline: central;
        }}
        .hint-text {{
            position: absolute;
            top: 10px;
            left: 15px;
            font-size: 12px;
            color: #64748b;
            background: rgba(255,255,255,0.9);
            padding: 4px 10px;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
            pointer-events: none;
            z-index: 10;
        }}
    </style>
</head>
<body>
    <div class="hint-text">💡 Click nodes to Expand/Collapse | Drag to Pan | Scroll to Zoom</div>
    <div id="mindmap-container"></div>
    <script>
        const data = {data_json};
        
        let i = 0, duration = 300, root;

        const container = d3.select("#mindmap-container");
        const svg = container.append("svg")
            .attr("width", "100%")
            .attr("height", "100%");

        const gContainer = svg.append("g");

        // Pan & Zoom support
        const zoom = d3.zoom()
            .scaleExtent([0.3, 2.5])
            .on("zoom", (event) => {{
                gContainer.attr("transform", event.transform);
            }});

        svg.call(zoom);

        // Center initially on left side
        svg.call(zoom.transform, d3.zoomIdentity.translate(120, window.innerHeight / 2).scale(0.85));

        // Use nodeSize for predictable vertical & horizontal spacing
        const tree = d3.tree().nodeSize([42, 260]);

        const diagonal = d3.linkHorizontal()
            .x(d => d.y)
            .y(d => d.x);

        root = d3.hierarchy(data, d => d.children);
        root.x0 = 0;
        root.y0 = 0;

        // Collapse starting from level 2
        if (root.children) {{
            root.children.forEach(d => {{
                if (d.children) d.children.forEach(collapse);
            }});
        }}

        update(root);

        function collapse(d) {{
            if (d.children) {{
                d._children = d.children;
                d._children.forEach(collapse);
                d.children = null;
            }}
        }}

        function update(source) {{
            tree(root);

            const nodes = root.descendants();
            const links = root.links();

            // Horizontal spacing per level
            nodes.forEach(d => {{ d.y = d.depth * 250; }});

            // --- LINKS ---
            const link = gContainer.selectAll('path.link')
                .data(links, d => d.target.id || (d.target.id = ++i));

            const linkEnter = link.enter().insert('path', 'g')
                .attr('class', 'link')
                .attr('d', d => {{
                    const o = {{ x: source.x0, y: source.y0 }};
                    return diagonal({{ source: o, target: o }});
                }});

            linkEnter.merge(link).transition().duration(duration)
                .attr('d', diagonal);

            link.exit().transition().duration(duration)
                .attr('d', d => {{
                    const o = {{ x: source.x, y: source.y }};
                    return diagonal({{ source: o, target: o }});
                }})
                .remove();

            // --- NODES ---
            const node = gContainer.selectAll('g.node')
                .data(nodes, d => d.id || (d.id = ++i));

            const nodeEnter = node.enter().append('g')
                .attr('class', 'node')
                .attr('transform', `translate(${{source.y0}}, ${{source.x0}})`)
                .on('click', (event, d) => {{
                    if (d.children) {{
                        d._children = d.children;
                        d.children = null;
                    }} else if (d._children) {{
                        d.children = d._children;
                        d._children = null;
                    }}
                    update(d);
                }});

            // Pill box dimensions calculated per node
            nodeEnter.append('rect')
                .attr('rx', 10)
                .attr('ry', 10)
                .attr('height', 34)
                .attr('y', -17)
                .attr('width', d => Math.max(140, d.data.name.length * 7.5 + 24))
                .attr('x', d => -Math.max(140, d.data.name.length * 7.5 + 24) / 2)
                .style('fill', d => {{
                    if (d.depth === 0) return '#c7d2fe'; // Root purple
                    if (d.depth === 1) return '#dbeafe'; // Level 1 blue
                    if (d.depth === 2) return '#bbf7d0'; // Level 2 green
                    return '#dcfce7';                   // Level 3 soft green
                }})
                .style('stroke', d => {{
                    if (d.depth === 0) return '#6366f1';
                    if (d.depth === 1) return '#3b82f6';
                    if (d.depth === 2) return '#22c55e';
                    return '#16a34a';
                }})
                .style('stroke-width', '1.5px');

            // Text Label
            nodeEnter.append('text')
                .text(d => d.data.name);

            // Toggle Button (< / >) on the right edge of expandable nodes
            const toggleGroup = nodeEnter.append('g')
                .attr('class', 'toggle-btn')
                .attr('transform', d => `translate(${{Math.max(140, d.data.name.length * 7.5 + 24) / 2}}, 0)`);

            toggleGroup.append('circle')
                .attr('r', 9);

            toggleGroup.append('text')
                .attr('class', 'toggle-text');

            // --- TRANSITIONS ---
            const nodeUpdate = nodeEnter.merge(node);

            nodeUpdate.transition().duration(duration)
                .attr('transform', d => `translate(${{d.y}}, ${{d.x}})`);

            nodeUpdate.select('.toggle-btn')
                .style('display', d => (d.children || d._children) ? 'block' : 'none');

            nodeUpdate.select('.toggle-text')
                .text(d => d.children ? '<' : '>');

            node.exit().transition().duration(duration)
                .attr('transform', `translate(${{source.y}}, ${{source.x}})`)
                .remove();

            nodes.forEach(d => {{
                d.x0 = d.x;
                d.y0 = d.y;
            }});
        }}
    </script>
</body>
</html>
"""


app_ui = ui.page_fluid(
    ui.h3("Fashion Supply Chain Management Mind Map"),
    ui.output_ui("mindmap_ui"),
)


def server(input, output, session):
    @render.ui
    def mindmap_ui():
        return ui.tags.iframe(
            srcdoc=build_horizontal_mindmap_html(mindmap_data),
            style="width: 100%; height: 850px; border: 1px solid #cbd5e1; border-radius: 12px; background: #fff;",
        )


app = App(app_ui, server)

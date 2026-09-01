import json
from shiny import App, render, ui

# Complete mind map hierarchy transcribed directly from your new image
mindmap_data = {
    "name": "Fashion Supply Chain Management (Chapters 1-3)",
    "children": [
        {
            "name": "Supply Chain Foundations (Chapter 1)",
            "children": [
                {
                    "name": "Definition and Scope (Chapter 1)",
                    "children": [
                        {
                            "name": (
                                "Complex Collaboration of Stakeholders"
                                " (Chapter 1)"
                            )
                        },
                        {
                            "name": (
                                "Seamless Production and Delivery (Chapter 1)"
                            )
                        },
                        {
                            "name": (
                                "Key Contributors: Logistics and Inventory"
                                " (Chapter 1)"
                            )
                        },
                        {
                            "name": (
                                "The Lifeline of the Fashion Industry"
                                " (Chapter 1)"
                            )
                        },
                    ],
                },
                {
                    "name": "Historical Origins (Chapter 1)",
                    "children": [
                        {"name": "Military Influence: Art of War (Chapter 1)"},
                        {
                            "name": (
                                "Standardized Sizing and Mass Production"
                                " (Chapter 1)"
                            )
                        },
                        {
                            "name": (
                                "Civil War Ready-to-Wear Uniforms (Chapter 1)"
                            )
                        },
                        {
                            "name": (
                                "Peter Drucker: Management Principles"
                                " (Chapter 1)"
                            )
                        },
                    ],
                },
                {
                    "name": "Technological Evolution (Chapter 1)",
                    "children": [
                        {
                            "name": (
                                "Industrial Revolution: Sewing Machines"
                                " (Chapter 1)"
                            )
                        },
                        {
                            "name": (
                                "Ford's Assembly Line Principles (Chapter 1)"
                            )
                        },
                        {
                            "name": (
                                "Global Containerized Shipping (Chapter 1)"
                            )
                        },
                        {
                            "name": (
                                "Barcoding and UPC Standardization (Chapter 1)"
                            )
                        },
                        {"name": "EDI and MRP Systems (Chapter 1)"},
                    ],
                },
            ],
        },
        {
            "name": "The Global Supply Chain (Chapter 2)",
            "children": [
                {
                    "name": "Factors Impacting Sourcing (Chapter 2)",
                    "children": [
                        {"name": "Rising Labor Costs in China (Chapter 2)"},
                        {
                            "name": (
                                "Political Climate and Infrastructure"
                                " (Chapter 2)"
                            )
                        },
                        {
                            "name": (
                                "Proximity to Emerging Markets (Chapter 2)"
                            )
                        },
                        {"name": "Impact of Quotas on Strategy (Chapter 2)"},
                    ],
                },
                {
                    "name": "Manufacturing Models (Chapter 2)",
                    "children": [
                        {
                            "name": (
                                "Cut, Make, and Trim (CMT) Process (Chapter 2)"
                            )
                        },
                        {
                            "name": (
                                "Transactional vs. Strategic Partnerships"
                                " (Chapter 2)"
                            )
                        },
                        {
                            "name": (
                                "Efficiency through Collaborative Testing"
                                " (Chapter 2)"
                            )
                        },
                    ],
                },
                {
                    "name": "Regional Historical Roles (Chapter 2)",
                    "children": [
                        {"name": "US Economic Boom Post-WWII (Chapter 2)"},
                        {
                            "name": (
                                "Japan: Keiretsu and Technology Focus"
                                " (Chapter 2)"
                            )
                        },
                        {
                            "name": (
                                "South Korea: Textiles and Footwear Hub"
                                " (Chapter 2)"
                            )
                        },
                    ],
                },
            ],
        },
        {
            "name": "CSR and Sustainability (Chapter 3)",
            "children": [
                {
                    "name": "Core CSR Concepts (Chapter 3)",
                    "children": [
                        {
                            "name": (
                                "Responsibility for Societal Impact (Chapter 3)"
                            )
                        },
                        {
                            "name": (
                                "Catalysts for Change: Safety and Labor"
                                " (Chapter 3)"
                            )
                        },
                        {
                            "name": (
                                "Human and Environmental Justice (Chapter 3)"
                            )
                        },
                    ],
                },
                {
                    "name": "Key Participant Perspectives (Chapter 3)",
                    "children": [
                        {
                            "name": (
                                "Philanthropy: TOMS and Warby Parker"
                                " (Chapter 3)"
                            )
                        },
                        {
                            "name": (
                                "Ethical Design: Stella McCartney (Chapter 3)"
                            )
                        },
                        {
                            "name": (
                                "Consumer Awareness and Commitment (Chapter 3)"
                            )
                        },
                    ],
                },
                {
                    "name": "Tools and Standards (Chapter 3)",
                    "children": [
                        {
                            "name": (
                                "Evolution of Vendor Compliance (Chapter 3)"
                            )
                        },
                        {
                            "name": (
                                "Higg Index and Sustainability Metrics"
                                " (Chapter 3)"
                            )
                        },
                        {"name": "Fair Labor Association (Chapter 3)"},
                        {"name": "Third-Party Certifications (Chapter 3)"},
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
            font-size: 11.5px;
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
            .scaleExtent([0.2, 2.5])
            .on("zoom", (event) => {{
                gContainer.attr("transform", event.transform);
            }});

        svg.call(zoom);

        // Center initially on left side
        svg.call(zoom.transform, d3.zoomIdentity.translate(140, window.innerHeight / 2).scale(0.8));

        // Predictable vertical and horizontal spacing
        const tree = d3.tree().nodeSize([38, 350]);

        const diagonal = d3.linkHorizontal()
            .x(d => d.y)
            .y(d => d.x);

        root = d3.hierarchy(data, d => d.children);
        root.x0 = 0;
        root.y0 = 0;

        // Collapse starting from level 2 initially
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

            // Horizontal spacing per level to accommodate long text labels
            nodes.forEach(d => {{ d.y = d.depth * 320; }});

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

            // Dynamically calculate box width based on text length
            const getBoxWidth = (d) => Math.max(160, d.data.name.length * 7.2 + 30);

            nodeEnter.append('rect')
                .attr('rx', 10)
                .attr('ry', 10)
                .attr('height', 32)
                .attr('y', -16)
                .attr('width', d => getBoxWidth(d))
                .attr('x', d => -getBoxWidth(d) / 2)
                .style('fill', d => {{
                    if (d.depth === 0) return '#c7d2fe'; // Root Indigo
                    if (d.depth === 1) return '#dbeafe'; // Level 1 Blue
                    if (d.depth === 2) return '#dcfce7'; // Level 2 Green
                    return '#dcfce7';                   // Level 3 Green
                }})
                .style('stroke', d => {{
                    if (d.depth === 0) return '#6366f1';
                    if (d.depth === 1) return '#3b82f6';
                    if (d.depth === 2) return '#22c55e';
                    return '#22c55e';
                }})
                .style('stroke-width', '1.5px');

            // Text Label
            nodeEnter.append('text')
                .text(d => d.data.name);

            // Toggle Button (< / >) on the right edge
            const toggleGroup = nodeEnter.append('g')
                .attr('class', 'toggle-btn')
                .attr('transform', d => `translate(${{getBoxWidth(d) / 2}}, 0)`);

            toggleGroup.append('circle')
                .attr('r', 8.5);

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
    ui.h3("Fashion Supply Chain Management (Chapters 1-3) Mind Map"),
    ui.output_ui("mindmap_ui"),
)


def server(input, output, session):
    @render.ui
    def mindmap_ui():
        return ui.tags.iframe(
            srcdoc=build_horizontal_mindmap_html(mindmap_data),
            style=(
                "width: 100%; height: 880px; border: 1px solid #cbd5e1;"
                " border-radius: 12px; background: #fff;"
            ),
        )


app = App(app_ui, server)
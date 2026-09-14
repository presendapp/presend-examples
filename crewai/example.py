"""
Verified working example: using Presend's MCP server with CrewAI.
pip install -r requirements.txt
python example.py
"""
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "https://presend.pages.dev/mcp",
    "transport": "streamable-http",
}

with MCPServerAdapter(server_params) as tools:
    print(f"Discovered {len(tools)} tools from Presend's MCP server")
    print("First 5:", [t.name for t in tools[:5]])

    whois_tool = next(t for t in tools if t.name == "whois_lookup")
    result = whois_tool.run(domain="github.com")
    print("\nwhois_lookup(domain='github.com') result:")
    print(result)

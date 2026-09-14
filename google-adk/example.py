"""
Verified working example: using Presend's MCP server with Google's Agent Development Kit.
pip install -r requirements.txt
python example.py
"""
import asyncio
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams


async def main():
    toolset = McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url="https://presend.pages.dev/mcp",
        ),
    )
    tools = await toolset.get_tools()
    print(f"Discovered {len(tools)} tools from Presend's MCP server")
    print("First 5:", [t.name for t in tools[:5]])

    whois_tool = next(t for t in tools if t.name == "whois_lookup")
    result = await whois_tool.run_async(args={"domain": "github.com"}, tool_context=None)
    print("\nwhois_lookup(domain='github.com') result:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())

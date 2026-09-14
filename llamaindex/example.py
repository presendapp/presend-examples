"""
Verified working example: using Presend's MCP server with LlamaIndex.
pip install -r requirements.txt
python example.py
"""
import asyncio
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec


async def main():
    client = BasicMCPClient("https://presend.pages.dev/mcp")
    tools = await McpToolSpec(client=client).to_tool_list_async()
    print(f"Discovered {len(tools)} tools from Presend's MCP server")
    print("First 5:", [t.metadata.name for t in tools[:5]])

    whois_tool = next(t for t in tools if t.metadata.name == "whois_lookup")
    result = await whois_tool.acall(domain="github.com")
    print("\nwhois_lookup(domain='github.com') result:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())

"""
Verified working example: using Presend's MCP server with LangChain.
pip install -r requirements.txt
python example.py
"""
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient({
        "presend": {
            "url": "https://presend.pages.dev/mcp",
            "transport": "streamable_http",
        }
    })
    tools = await client.get_tools()
    print(f"Discovered {len(tools)} tools from Presend's MCP server")
    print("First 5:", [t.name for t in tools[:5]])

    whois_tool = next(t for t in tools if t.name == "whois_lookup")
    result = await whois_tool.ainvoke({"domain": "github.com"})
    print("\nwhois_lookup(domain='github.com') result:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())

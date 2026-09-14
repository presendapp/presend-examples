"""
Verified working example: using Presend's MCP server with OpenAI's Agents SDK.
pip install -r requirements.txt
python example.py
"""
import asyncio
from agents.mcp import MCPServerStreamableHttp


async def main():
    async with MCPServerStreamableHttp(
        params={"url": "https://presend.pages.dev/mcp"},
        name="presend",
    ) as server:
        tools = await server.list_tools()
        print(f"Discovered {len(tools)} tools from Presend's MCP server")
        print("First 5:", [t.name for t in tools[:5]])

        result = await server.call_tool("whois_lookup", {"domain": "github.com"})
        print("\nwhois_lookup(domain='github.com') result:")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())

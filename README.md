# Presend Examples

Working, tested code examples for using [Presend](https://presend.pages.dev)'s free API and MCP server -- no signup, no API key required for any of these.

Each example connects to Presend's live MCP server (`https://presend.pages.dev/mcp`) or REST API (`https://presend.pages.dev/api`) and runs a real `whois_lookup` call on `github.com`.

| Framework | Folder | Install |
|---|---|---|
| LangChain | [`langchain/`](langchain/) | `pip install -r langchain/requirements.txt` |
| CrewAI | [`crewai/`](crewai/) | `pip install -r crewai/requirements.txt` |
| LlamaIndex | [`llamaindex/`](llamaindex/) | `pip install -r llamaindex/requirements.txt` |
| OpenAI Agents SDK | [`openai-agents/`](openai-agents/) | `pip install -r openai-agents/requirements.txt` |
| Google ADK | [`google-adk/`](google-adk/) | `pip install -r google-adk/requirements.txt` |
| Plain REST (no MCP) | [`rest-api/`](rest-api/) | none, stdlib only |

Run any example with:

```bash
cd <framework-folder>
pip install -r requirements.txt
python example.py
```

## For teams

We are testing a paid offer for teams: the same dependency checks on every pull request that changes a dependency and for AI coding agents before they install a package, with false-positive rates measured and published. Nothing is for sale yet. If your team would use it, [join the waitlist](https://presend.pages.dev/teams).

## What is Presend?

A free security/utility API and an MCP server, plus 48 free browser-based file tools. No signup, no API key.

- **API docs**: https://presend.pages.dev/api
- **OpenAPI spec**: https://presend.pages.dev/openapi.json
- **MCP server**: https://presend.pages.dev/mcp
- **Main repo**: https://github.com/presendapp/presend-source

The endpoint used in every example here, `maintainer-change-check`, flags an npm package whose publisher changed after a long period of dormancy -- the pattern behind the `event-stream` compromise (2018). It cannot detect a hijacked existing account (`ua-parser-js`) or a malicious release by the original maintainer (`colors.js`).

## License

MIT

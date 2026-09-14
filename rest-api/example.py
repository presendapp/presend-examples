"""
Verified working example: calling Presend's REST API directly, no MCP,
no framework -- just plain HTTP. No signup, no API key.
python example.py
"""
import urllib.request
import json

BASE = "https://presend.pages.dev/api"


def call(endpoint, params=""):
    url = f"{BASE}/{endpoint}{params}"
    # Explicit User-Agent required -- Cloudflare blocks urllib's default one.
    req = urllib.request.Request(url, headers={"User-Agent": "presend-examples/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


if __name__ == "__main__":
    print("maintainer-change-check on lodash:")
    print(json.dumps(call("maintainer-change-check", "?ecosystem=npm&package=lodash"), indent=2))

    print("\nvulnerability-check on lodash:")
    result = call("vulnerability-check", "?ecosystem=npm&package=lodash")
    print(f"  {len(result.get('vulnerabilities', []))} known vulnerabilities found")

    print("\nwhois-lookup on github.com:")
    print(json.dumps(call("whois-lookup", "?domain=github.com"), indent=2))

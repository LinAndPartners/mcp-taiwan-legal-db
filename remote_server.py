import os
from mcp_server.server import mcp
if __name__ == "__main__":
  mcp.settings.host = "0.0.0.0"
  mcp.settings.port = int(os.environ.get("PORT", "10000"))
  mcp.run(transport="sse")

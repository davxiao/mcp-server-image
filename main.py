from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("My Server")

@mcp.tool
def hello_world(input: str) -> str:
    """Say hello on the server"""
    return f"Hello {input}, today's date is {datetime.now().date()}" 

# Create ASGI application
app = mcp.streamable_http_app()


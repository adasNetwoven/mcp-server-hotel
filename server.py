from fastmcp import FastMCP

import os
#port = int(os.getenv("PORT", 8000))
# Create MCP server
mcp = FastMCP("hotels")


# Get Hotel reviews - a tool which takes hotel name as input and returns 10 latest reviews
@mcp.tool()
def get_hotel_reviews(hotel_name: str) -> str:
    """Get latest 10 reviews for a hotel"""
    return "Here are the latest 10 reviews for {}: [Review1, Review2, Review3, Review4, Review5, Review6, Review7, Review8, Review9, Review10]".format(hotel_name)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))

    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port
    )
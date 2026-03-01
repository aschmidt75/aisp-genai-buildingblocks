"""Main entry point for running the Weather MCP Server"""

import argparse
import json
import logging
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weather MCP Server")
    parser.add_argument(
        "--dump-config",
        action="store_true",
        help="Dump the MCP server definition for mcp.json and exit"
    )
    args = parser.parse_args()
    
    if args.dump_config:
        # Disable logging for clean JSON output
        logging.disable(logging.CRITICAL)
        # Import the server to ensure tools are registered
        from src.weather_server import mcp
        # Generate the MCP server definition for mcp.json
        config = {
            "mcpServers": {
                "aisp-mcp-bridge": {
                    "command": "uv",
                    "args": [
                        "--directory",
                        "/Users/andreas/code/ai-playgrounds/aisp-genai-buildingblocks/aisp-mcp-bridge",
                        "run",
                        "main.py"
                    ]
                }
            }
        }
        print(json.dumps(config, indent=2))
        sys.exit(0)
    
    # Import the server to ensure tools are registered
    from src.weather_server import mcp
    
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    
    logger.info("Starting Weather MCP Server...")
    logger.info("The server will listen on stdio for MCP protocol messages")
    logger.info("Press Ctrl+C to stop the server")
    
    # Run the MCP server
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)

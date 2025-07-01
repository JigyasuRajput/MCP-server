import asyncio
from mcp_server import main

if __name__ == "__main__":
    print("🚀 Starting PuchAI MCP Server...")
    print("📱 Phone: 919811227106")
    print("🔑 Token: 85b4b747f1cc")
    print("🌐 Server will be available at: http://localhost:8085")
    print("📝 Make sure you have your resume.md file in this directory")
    print("\nPress Ctrl+C to stop the server\n")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")

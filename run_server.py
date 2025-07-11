#!/usr/bin/env python3
import sys
import os

# appディレクトリをPythonパスに追加
app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server')
sys.path.insert(0, app_dir)

try:
    from main import server
    from config import settings
    
    if __name__ == "__main__":
        import uvicorn
        print(f"Starting server on {settings.host}:{settings.port}")
        uvicorn.run(server, host=settings.host, port=settings.port)
        
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure you're running this script from the project root directory")
    sys.exit(1)
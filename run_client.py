#!/usr/bin/env python3
import sys
import os
import asyncio

# clientディレクトリをPythonパスに追加
client_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'client')
sys.path.insert(0, client_dir)

try:
    from main import main
    
    if __name__ == "__main__":
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print("\nGoodbye!")
        except Exception as e:
            print(f"Fatal error: {e}")
            
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure you're running this script from the project root directory")
    sys.exit(1)
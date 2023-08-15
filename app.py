import sys
import uvicorn
from src.server.app import api_server

if __name__ == "__main__":

    if len(sys.argv) != 2:
        port = 5000
    else:
        port = int(sys.argv[1])
    uvicorn.run(api_server(), port=port)

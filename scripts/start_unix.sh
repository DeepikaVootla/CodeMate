#!/bin/bash  
echo "[*] Starting CommandExecBridge (Linux/macOS)"  
uvicorn command_exec_bridge:app --port 3333  
echo "Server running on http://localhost:3333" 

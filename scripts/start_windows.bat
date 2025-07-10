@echo off  
echo [*] Starting CommandExecBridge (Windows)  
uvicorn bridge.command_exec_bridge:app --port 3333  
pause 

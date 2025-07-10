from fastapi import FastAPI, Request, HTTPException  
from pydantic import BaseModel  
import subprocess  
import platform  
  
API_KEY = "execbot-bridge-key"  
  
app = FastAPI(title="Command Execution Bridge")  
  
class CommandRequest(BaseModel):  
    command: str  
  
@app.get("/health")  
def health():  
    return {"status": "ok"}  
  
@app.post("/run")  
def run_shell_command(payload: CommandRequest, request: Request):  
    if request.headers.get("x-api-key") != API_KEY:  
        raise HTTPException(status_code=401, detail="Unauthorized")  
  
    try:  
        system = platform.system().lower()  
        result = subprocess.run(payload.command, shell=True, capture_output=True, text=True)  
        
        print(f"Command received from relay: {payload.command}")
        print(f"Command output: {result.stdout.strip()}")

        return {  
            "os": system,  
            "output": result.stdout.strip(),  
            "error": result.stderr.strip(),  
            "returncode": result.returncode  
        }  
    except Exception as e:  
        return {"error": str(e)} 

"# I can read this when the connection's open ;)" 

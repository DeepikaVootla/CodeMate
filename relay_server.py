from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel  
import httpx  
  
app = FastAPI(title="ExecBot Relay Server")  
  
class RelayPayload(BaseModel):  
    username: str  
    command: str  
  
@app.post("/run")  
async def relay_command(data: RelayPayload):  

    print(f"Received command from GPT: {data.command} for user: {data.username}")

    target_url = f"https://134f55279957.ngrok-free.app/run"  
    headers = {"x-api-key": "execbot-bridge-key"}  
  
    try:  
        async with httpx.AsyncClient(timeout=10) as client:  
            response = await client.post(target_url, json={"command": data.command}, headers=headers)  
            response.raise_for_status()  
            return response.json()  
    except Exception as e:  
            raise HTTPException(status_code=500, detail=str(e))


# GPT Command Execution Bridge for Windows/macOS/Linux  
  
## Requirements  
- Python 3.8+  
- pip  
- [ngrok](https://ngrok.com/download)  
  
---  
  
## Windows Setup  
1. Open PowerShell  
2. Run: `pip install -r requirements.txt`  
3. Run: `scripts\start_windows.bat`  
4. In another terminal: `ngrok http 3333`  
  
---  
  
## macOS/Linux Setup  
1. Open Terminal  
2. Run: `pip install -r bridge/requirements.txt`  
3. Make the script executable: `chmod +x scripts/start_unix.sh`  
4. Start the server: `./scripts/start_unix.sh`  
5. In another terminal: `ngrok http 3333`  

---

This will output a random ngrok URL (e.g., https://<random_subdomain>.ngrok-free.app).

Copy the URL provided by ngrok.

## Update the relay_server.py file:

Open relay_server.py in the relay folder.

Update the target_url to match your newly generated ngrok URL:
target_url = "https://<random_subdomain>.ngrok-free.app/run"

Replace <random_subdomain> with your actual ngrok URL.

Give the ngrok URL generated in the target_url to the GPT, in your chat.
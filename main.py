from fastapi import FastAPI, Request
from user_agents import parse

app = FastAPI()


@app.get("/device-info")
async def get_device_info(request: Request):
    user_agent_str = request.headers.get('user-agent')
    user_agent = parse(user_agent_str)
    client_ip = request.client.host

    device_info = {
        "user_agent": user_agent_str,
        "is_bot": user_agent.is_bot,
        "is_mobile": user_agent.is_mobile,
        "is_tablet": user_agent.is_tablet,
        "is_pc": user_agent.is_pc,
        "browser": user_agent.browser.family,
        "browser_version": user_agent.browser.version_string,
        "os": user_agent.os.family,
        "os_version": user_agent.os.version_string,
        "device": user_agent.device.family,
    }

    print(f"Device Info: {device_info}")
    print(f"Client IP Address: {client_ip}")

    return {
        "device_info": device_info,
        "ip_address": client_ip
    }

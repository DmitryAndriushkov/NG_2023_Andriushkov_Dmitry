import json
import socket
import platform
import psutil

print("\nHi! This program display some information about pc\nHere's some info:")

pcInfo = {
    "OS": platform.system(),
    "Version": platform.uname().release,
    "Hostname": socket.gethostname(),
    "IP": socket.gethostbyname(socket.gethostname()),
    "RAM": psutil.virtual_memory().total / 1e9,
    "CPU": {
        "Cores": psutil.cpu_count(logical=0),
        "Frequency": psutil.cpu_freq().current,
        "Usage": psutil.cpu_percent(interval=1)
    },
}
print(json.dumps(pcInfo, indent=4, separators=(" ", " ---> ")))
import platform

def get_os_info() -> dict:
  info = {
    "sistema_operacional": platform.system(),
  }
  return info

print(get_os_info())
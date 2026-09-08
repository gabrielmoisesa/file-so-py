import platform
import socket
import os

def get_os_info() -> dict:
  info = {
    "sistema_operacional": platform.system(),
    "release": platform.release(),
    "versao": platform.version(),
    "arquitetura": platform.machine(),
    "nome_maquina": socket.gethostname(),
    "usuario": os.getlogin(),
    "versao_python": platform.python_version(),
  }
  return info

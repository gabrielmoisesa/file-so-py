import json
import os

def create_file(path: str, data: dict) -> None:
  try:
    with open(path, "w", encoding="utf-8") as file:
      json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Arquivo '{path}' criado com sucesso.")
  except PermissionError:
    print(f"Erro: sem permissão para criar '{path}'.")
  except TypeError:
    print(f"Erro: os dados informados não podem ser convertidos para JSON.")
  except OSError as e:
    print(f"Erro ao criar o arquivo '{path}': {e}")

def read_file(path: str) -> dict | None:
  try:
    with open(path, "r", encoding="utf-8") as file:
      return json.load(file)
  except FileNotFoundError:
    print(f"Erro: o arquivo '{path}' não existe.")
    return None
  except json.JSONDecodeError:
    print(f"Erro: o arquivo '{path}' não contém um JSON válido.")
    return None
  except PermissionError:
    print(f"Erro: sem permissão para ler o arquivo '{path}'.")
    return None
  except OSError as e:
    print(f"Erro ao ler o arquivo '{path}': {e}")
    return None

def rename_file(current_path: str, new_path: str) -> bool:
  try:
    os.rename(current_path, new_path)
    print(f"Arquivo renomeado para '{new_path}'.")
    return True
  except FileNotFoundError:
    print(f"Erro: o arquivo '{current_path}' não existe.")
  except FileExistsError:
    print(f"Erro: já existe um arquivo com o nome '{new_path}'.")
  except PermissionError:
    print(f"Erro: sem permissão para renomear o arquivo '{current_path}'.")
  except OSError as e:
    print(f"Erro ao renomear o arquivo '{current_path}': {e}")
  return False

def delete_file(path: str) -> None:
  try:
    os.remove(path)
    print(f"Arquivo '{path}' excluído com sucesso.")
  except FileNotFoundError:
    print(f"Erro: o arquivo '{path}' não existe.")
  except PermissionError:
    print(f"Erro: sem permissão para excluir o arquivo '{path}'.")
  except OSError as e:
    print(f"Erro ao excluir o arquivo '{path}': {e}")

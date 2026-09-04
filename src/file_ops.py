import json

def create_file(path: str, data: dict) -> None:
  with open(path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
  print(f"Arquivo '{path}' criado com sucesso.")

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
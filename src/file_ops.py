import json

def create_file(path: str, data: dict) -> None:
  with open(path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
  print(f"Arquivo '{path}' criado com sucesso.")
  
from file_ops import create_file, read_file, rename_file, delete_file

def main() -> None:
  file_path = "info_so.json"

  create_file(file_path, {"SO": "Linux", "Status": "Teste"})
  print(read_file(file_path))

  rename_file(file_path, "info_renomeado_so.json")

  delete_file("info_renomeado_so.json")
  delete_file("info_renomeado_so.json")

if __name__ == "__main__":
    main()
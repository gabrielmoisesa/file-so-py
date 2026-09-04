from file_ops import create_file, read_file

def main() -> None:
  file_path = "info_so.json"

  create_file(file_path, {"SO": "Linux", "Status": "Teste"})
  print(read_file(file_path))

if __name__ == "__main__":
    main()
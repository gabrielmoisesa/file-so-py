from file_ops import create_file

def main() -> None:
  file_path = "info_so.json"

  create_file(file_path, {"SO": "Linux", "Status": "Teste"})

if __name__ == "__main__":
    main()
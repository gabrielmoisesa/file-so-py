from file_ops import create_file, read_file, rename_file, delete_file
from sys_info import get_os_info

def show_menu() -> None:
    print("\n=== FileSO.py ===")
    print("1. Criar arquivo com informações do SO")
    print("2. Ler arquivo")
    print("3. Renomear arquivo")
    print("4. Excluir arquivo")
    print("5. Sair")

def main() -> None:
  file_path = "info_so.json"

  while True:
     show_menu()
     selected_option = input("Escolha uma opção: ").strip()

     if selected_option == "1":
        info = get_os_info()
        print()
        create_file(file_path, info)

     elif selected_option == "2":
        data = read_file(file_path)
        if data:
            print(f"\n======== {file_path} ========")
            for chave, valor in data.items():
                print(f"{chave}: {valor}")

     elif selected_option == "3":
        new_path = input("Novo nome/caminho do arquivo (ex: dados.json): ").strip()
        if rename_file(file_path, new_path):
           file_path = new_path

     elif selected_option == "4":
        delete_file(file_path)

     elif selected_option == "5":
        print("Encerrando o programa...")
        break

     else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
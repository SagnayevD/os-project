import os

def search_files(folder_path, file_name, file_extension):
    found_files = []
    
    try:
        if not os.path.exists(folder_path):
            raise ValueError("Указанной папки не существует.")
        
        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.startswith(file_name) and entry.name.endswith(file_extension):
                    found_files.append(entry.path)
    except OSError as e:
        print("Ошибка при сканировании папки:", e)
    except ValueError as ve:
        print(ve)
    
    return found_files

if __name__ == "__main__":
    try:
        folder_path = input("Введите путь к папке для поиска: ")
        file_name = input("Введите имя файла или его начало: ")
        file_extension = input("Введите расширение файла (например, '.txt'): ")
        
        result = search_files(folder_path, file_name, file_extension)
        if result:
            print("Найденные файлы:")
            for file_path in result:
                print(file_path)
        else:
            print("Файлы с указанным именем и расширением не найдены.")
    except KeyboardInterrupt:
        print("Операция прервана пользователем.")
    except Exception as e:
        print("Произошла ошибка:", e)

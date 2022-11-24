import os

class FileSystem:
    def __init__(self, cpf: str):
        self.cpf: cpf = cpf
        self.path: str = './src/data/'
        self.folder_path: str = os.path.join(self.path, self.cpf)

    def create_file(self, file_name: str, file: bytes) -> bool: 

        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        try:
            with open(os.path.join(self.folder_path, file_name), 'xb') as f:
                f.write(file)
        except Exception as e:
            return False
        
        return True
    
    def read_file(self, file_name: str) -> bytes:

        file_path = os.path.join(self.folder_path, file_name)

        if not os.path.isfile(file_path): return None

        try:
            with open(file_path, 'rb') as f:
                file: bytes = f.read()
        except Exception as e:
            return None
        
        return file
    
    def update_file(self, file_name: str, file: bytes) -> bool:

        file_path = os.path.join(self.folder_path, file_name)

        if not os.path.isfile(file_path): return False
        if not os.path.exists(self.folder_path): return False

        try:
            with open(os.path.join(self.folder_path, file_name), 'wb') as f:
                f.write(file)
        except Exception as e:
            return False
        
        return True
    
    def delete_file(self, file_name: str) -> bool:
        file_path = os.path.join(self.folder_path, file_name)

        if not os.path.isfile(file_path): return False
        if not os.path.exists(self.folder_path): return False

        try:
            os.remove(file_path)
        except Exception as e:
            return False
        
        return True
    
    def list_files(self) -> list:        

        if not os.path.exists(self.folder_path): return None

        return os.listdir(self.folder_path)

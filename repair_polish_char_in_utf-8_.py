import os

folder_path = '.'

replacements = [('±', 'ą'), ('ê', 'ę'), ('³', 'ł'), ('æ', 'ć'), ('ñ', 'ń'), ('¼', 'ź'), ('¶', 'ś'), ('¿', 'ż'), ('ó', 'ó'), ('¡', 'Ą'), ('Æ', 'Ć'), ('Ê', 'Ę'), ('£', 'Ł'), ('Ñ', 'Ń'), ('Ó', 'Ó'), ('¦', 'Ś'), ('¬', 'Ż'), ('¯', 'Ź')]

for filename in os.listdir(folder_path):
    if filename.endswith(".htm"):
        file_path = os.path.join(folder_path, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                for original, replacement in replacements:
                    content = content.replace(original, replacement)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
                
            print(f"Plik {file_path} został zaktualizowany.")
        except Exception as e:
            print(f"Błąd podczas przetwarzania pliku {file_path}: {e}")
import os

class FileHandler:
    @staticmethod
    def read_file(filepath):
        """
        Read contents of a file
        
        Args:
            filepath (str): Path to the file
        
        Returns:
            str: File contents
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return ""
    
    @staticmethod
    def save_file(filepath, content):
        """
        Save content to a file
        
        Args:
            filepath (str): Path to save the file
            content (str): Content to write
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            print(f"Error saving file {filepath}: {e}")
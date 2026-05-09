import os

def read_template(template_path):
    """
    Reads an HTML or text template file and returns its content.
    """
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Template file not found at {template_path}")
        return ""
    except Exception as e:
        print(f"Error reading template: {e}")
        return ""

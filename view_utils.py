import os
import json

directory_path_available = "/etc/nginx/sites-available/"

def show_all_subDomain():
      file_names = os.listdir(directory_path_available)
      data = [[part for part in name.split('.')] for name in file_names]
      return json.dumps(data)

def demo_site_nginx():
      file_path = "logCreateSubDomain.txt"
      lines_to_read = 10
      last_lines = []
      with open(file_path, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()
            last_lines = all_lines[-lines_to_read:]
      return json.dumps(last_lines)

def search_name_subDomain(nameSearch):
      nameSearch = nameSearch.lower()
      file_names = os.listdir(directory_path_available)
      for file_name in file_names:
            if nameSearch in file_name.lower():
                  return json.dumps(file_name.split('.'))
      return json.dumps(["not found"])

def search_port_subDomain(portSearch):
      portSearch = str(portSearch)
      file_names = os.listdir(directory_path_available)
      results = []
      for file_name in file_names:
            name, _, port = file_name.rpartition('.')
            if port == portSearch:
                  results.append(file_name.split('.'))
      return json.dumps(results if results else ["not found"])

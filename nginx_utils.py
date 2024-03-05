import subprocess
import os
from templates import nginx_conf_template
from file_utils import save_errors_to_file, save_date_create_to_file
from view_utils import directory_path_available

def create_nginx_config(sub_domain, port):
      try:
            nginx_conf_content = nginx_conf_template.render(sub_domain=sub_domain, port=port)
            nginx_conf_path = f"/etc/nginx/sites-available/{sub_domain}.{port}"
            if os.path.exists(nginx_conf_path):
                return "Configuration file already exists"
        
            with open(nginx_conf_path, 'w') as file:
                  file.write(nginx_conf_content)
        
            subprocess.run(['ln', '-s', nginx_conf_path, f"/etc/nginx/sites-enabled/{sub_domain}"])
            subprocess.run(['systemctl', 'restart', 'nginx'])
        
            save_date_create_to_file(f"subDomain : {sub_domain}, port : {port} created", f"{sub_domain}.{port}")
        
            return "Nginx configuration created successfully."
      except Exception as e:
            error_message = f"Error creating nginx config for {sub_domain}: {str(e)}"
            save_errors_to_file(error_message)
            return "Failed to create nginx configuration."

def delete_subDomain_nginx(deleteNameFile):
      try:
            file_names = os.listdir(directory_path_available)
            for file_name in file_names:
                  for i in range(0, min(len(deleteNameFile), len(file_name))):
                        if deleteNameFile[i] != file_name[i]:
                              break
                  else:
                        subprocess.run(['unlink', f"/etc/nginx/sites-enabled/{file_name}"])
                        os.remove(f"/etc/nginx/sites-available/{file_name}")
                        subprocess.run(['systemctl', 'restart', 'nginx'])
                        return f"File {deleteNameFile} deleted successfully"
            else:
                  return f"File {deleteNameFile} not found"                  
                              
            
      except Exception as e:
            save_errors_to_file(str(e))
            return "Failed to delete subdomain configuration."

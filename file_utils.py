import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_errors_to_file(error_message):
      with open('errors.txt', 'a') as file: 
            file.write(f"{timestamp}: {error_message}\n")

def save_date_create_to_file(message, name):
      with open('logCreateSubDomain.txt', 'a') as file: 
            file.write(f"{name}{timestamp} -> {message}\n")

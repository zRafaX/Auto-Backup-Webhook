import requests
import shutil
import os
import tempfile
from datetime import datetime
import time

def send_backup_to_webhook(backup_path):
    webhook_url = os.getenv('WEBHOOK')

    restart_message = {
        'content': '🔄️ Backup:',
        'username': 'Backup'
    }

    files = {'file': (f'MY_DATABASE_{datetime.now().strftime("%Y%m%d%H%M%S")}.zip', open(backup_path, 'rb'))}

    response = requests.post(webhook_url, data=restart_message, files=files)

    if response.status_code == 200:
        print('✅ Backup sent!')
    else:
        print(f'Error sending backup. Status code: {response.status_code}')

def create_backup():
    folder_path = './'

    backup_filename = f'MY_DATABASE_{datetime.now().strftime("%Y%m%d%H%M%S")}.zip'

    backup_folder_path = './Backup'

    if os.path.exists(backup_folder_path):
        shutil.rmtree(backup_folder_path)

    temp_dir = tempfile.mkdtemp()

    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [d for d in dirs if d not in ['.cache', '.local']]

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(temp_dir, os.path.relpath(src_file, folder_path))
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            shutil.copy2(src_file, dest_file)

    backup_path = os.path.join(backup_folder_path, backup_filename)
    shutil.make_archive(backup_path[:-4], 'zip', temp_dir)

    shutil.rmtree(temp_dir)

    return backup_path

if __name__ == '__main__':
    while True:
        backup_path = create_backup()
        send_backup_to_webhook(backup_path)
        time.sleep(3600)
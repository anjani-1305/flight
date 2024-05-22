import os
import subprocess



# Path to your Django project's manage.py script
manage_py = r'C:\Users\Lenovo\Desktop\Flight\myproject\manage.py'

# Name of your Django management command
management_command = 'fetch_data'

# Construct the command to execute your management command
command = [ manage_py, management_command]

# Execute the command using subprocess
subprocess.run(command, check=True)

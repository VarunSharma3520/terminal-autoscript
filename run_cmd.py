import subprocess

def cmd_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            command = file.read().strip()
            subprocess.run(['powershell', '-Command', command], check=True) # for PowerShell (Windows)
            # subprocess.run(['bash', '-c', command], check=True) # for Bash
            return command

    except FileNotFoundError:
        print("File not found:", file_path)
    except subprocess.CalledProcessError as e:
        print("PowerShell Error:", e)

# Example usage:
file_path = 'command.txt'
print(cmd_from_file(file_path))

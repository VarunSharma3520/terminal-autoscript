import platform
import os

def run_command(command):
    print(f"Upcoming Command: {command}")
    permission = input("[Y/n] for next step: ").lower()
    if permission != "n":
        print("\n")
        os.system(command)

def cmd_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            commands = [line.strip() for line in file.readlines() if line.strip()]
            for command in commands:
                run_command(command)

    except FileNotFoundError:
        print("File not found:", file_path)

# Example usage:
file_path = 'command.txt'
cmd_from_file(file_path)

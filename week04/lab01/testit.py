import os
import subprocess

class DirectoryExecutor:
    def __init__(self):
        self.current_directory = os.getcwd()

    def construct_command(self):
        base_name = os.path.basename(self.current_directory)
        return f'python3 ../.check/__pycache__/test_{base_name}.cpython-310.pyc'

    def execute_command(self):
        command = self.construct_command()
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    executor = DirectoryExecutor()
    executor.execute_command()

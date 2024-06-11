import subprocess
import sys
import os

class Install:
    @staticmethod
    def run_pip_command(command, verbose=False):
        python_exe = sys.executable
        if sys.platform.startswith("win"):
            python_exe = os.path.join(sys.prefix, "pythonw.exe")
        
        try:
            # Se verbose for True, capture output; se não, não capture
            process = subprocess.run([python_exe, "-m", "pip"] + command,
                                     check=True, capture_output=not verbose,
                                     text=True)
            output = process.stdout
        except subprocess.CalledProcessError as cpe:
            output = cpe.stdout + cpe.stderr
            # Exibe a saída do erro independentemente do modo verbose
            print("Error occurred during pip command:", output)
            return
        
        if verbose:
            print(output)

    @staticmethod
    def from_requirements(file_path, verbose=False):
        Install.run_pip_command(["install", "-r", file_path], verbose)

    @staticmethod
    def module(package_name, verbose=False):
        Install.run_pip_command(["install", package_name], verbose)

    @staticmethod
    def modules(package_list, verbose=False):
        Install.run_pip_command(["install"] + package_list, verbose)

install = Install()

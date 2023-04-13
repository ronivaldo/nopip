import subprocess
import sys

class Install:
    @staticmethod
    def run_pip_command(command):
        subprocess.check_call([sys.executable, "-m", "pip"] + command)

    @staticmethod
    def from_requirements(file_path):
        Install.run_pip_command(["install", "-r", file_path])

    @staticmethod
    def module(package_name):
        Install.run_pip_command(["install", package_name])

    @staticmethod
    def modules(package_list):
        Install.run_pip_command(["install"] + package_list)

install = Install()

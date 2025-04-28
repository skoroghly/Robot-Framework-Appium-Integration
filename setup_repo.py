import os
import subprocess

def clone_and_setup_repo():
    repo_url = "<INSERT_REPO_URL_HERE>"
    clone_dir = "Robot_Framework_Appium_Integration"

    # Clone the repository
    if not os.path.exists(clone_dir):
        subprocess.run(["git", "clone", repo_url, clone_dir], check=True)
    else:
        print(f"Directory '{clone_dir}' already exists. Skipping clone.")

    # Change directory to the cloned repository
    os.chdir(clone_dir)

    # Install requirements
    requirements_file = "requirements.txt"
    if os.path.exists(requirements_file):
        subprocess.run(["pip", "install", "-r", requirements_file], check=True)
    else:
        print(f"'{requirements_file}' not found. Skipping requirements installation.")

if __name__ == "__main__":
    clone_and_setup_repo()
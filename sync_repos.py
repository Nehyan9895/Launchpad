import os
import shutil
import hashlib

CORE_REPO = "CoreRepo"
CLIENT_REPOS = ["ClientRepo1", "ClientRepo2"]
DLL_FILES = ["Add.dll", "Subtract.dll", "Multiply.dll", "Divide.dll"]

def hash_file(file_path):
    """Generate a hash for a file's content."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def sync_dlls():
    """Sync DLLs from the core repository to client repositories."""
    print("Starting DLL synchronization...")
    for dll in DLL_FILES:
        core_file = os.path.join(CORE_REPO, dll)
        core_hash = hash_file(core_file)

        for repo in CLIENT_REPOS:
            client_file = os.path.join(repo, dll)
            client_hash = hash_file(client_file)

            if core_hash != client_hash:
                shutil.copy2(core_file, client_file)
                print(f"Updated {dll} in {repo}")

if __name__ == "__main__":
    sync_dlls()

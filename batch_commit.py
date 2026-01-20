import os
import subprocess
import re

def run_git(args):
    result = subprocess.run(args, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Error running {' '.join(args)}: {result.stderr}")
    return result.stdout.strip()

def main():
    # 1. Get status
    status_output = run_git(["git", "status", "--porcelain"])
    
    files = []
    for line in status_output.split("\n"):
        if not line: continue
        # code is first 2 chars, then space, then filename (handle quotes if needed)
        # porcelain v1: XY PATH
        path = line[3:]
        path = path.strip('"') # Remove quotes if present
        files.append(path)

    print(f"Found {len(files)} changed files.")

    # Regex for submodules: docs/modules/X/submodules/Y/README.md
    submod_pattern = re.compile(r"docs[\\/]modules[\\/]([^\\/]+)[\\/]submodules[\\/]([^\\/]+)[\\/]README\.md", re.IGNORECASE)
    # Regex for modules: docs/modules/X/README.md
    mod_pattern = re.compile(r"docs[\\/]modules[\\/]([^\\/]+)[\\/]README\.md", re.IGNORECASE)

    for file_path in files:
        # Normalize path separators
        norm_path = file_path.replace("/", "\\")
        
        if "SESSION_HANDOFF.md" in norm_path:
            continue
            
        # Determine Commit Message
        commit_msg = ""
        
        submod_match = submod_pattern.search(norm_path)
        mod_match = mod_pattern.search(norm_path)
        
        if submod_match:
            module_name = submod_match.group(1)
            submodule_name = submod_match.group(2)
            commit_msg = f"docs: Enhance documentation for Submodule {submodule_name}"
        elif mod_match:
            module_name = mod_match.group(1)
            commit_msg = f"docs: Enhance overview for Module {module_name}"
        elif "generate_docs.py" in norm_path:
            commit_msg = "chore: update documentation generation script"
        elif ".gitignore" in norm_path:
            commit_msg = "chore: update gitignore"
        else:
            # Fallback for other files
            commit_msg = f"chore: update {os.path.basename(norm_path)}"

        # Add and Commit
        print(f"Committing {norm_path}...")
        run_git(["git", "add", file_path])
        run_git(["git", "commit", "-m", commit_msg])

    # Push at the end
    print("Pushing to remote...")
    run_git(["git", "push"])
    print("Done.")

if __name__ == "__main__":
    main()

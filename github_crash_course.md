### **Crash Course on Git and GitHub**

This crash course will provide an overview of Git and GitHub along with essential commands to get started. By the end of this guide, you'll have the foundational knowledge to work with version control effectively.

---

### **What is Git?**
Git is a distributed version control system that allows multiple developers to work on a project simultaneously while tracking changes.

### **What is GitHub?**
GitHub is a cloud-based platform for hosting Git repositories. It provides collaboration features such as pull requests, issues, and CI/CD.

---

### **Installing Git**
1. **Windows**: Download and install from [Git's official site](https://git-scm.com/).
2. **Mac**: Use Homebrew:  
   ```bash
   brew install git
   ```
3. **Linux**: Use your package manager:  
   ```bash
   sudo apt install git  # For Debian-based distros
   sudo yum install git  # For Red Hat-based distros
   ```

---

### **Git Setup**
Set up your Git environment:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

Check your configuration:
```bash
git config --list
```

---

### **Basic Git Commands**

#### **1. Create or Clone a Repository**
- **Initialize a new repository:**
  ```bash
  git init
  ```
- **Clone an existing repository:**
  ```bash
  git clone <repository_url>
  ```

#### **2. Stage and Commit Changes**
- **Check the status of your repo:**
  ```bash
  git status
  ```
- **Add files to the staging area:**
  ```bash
  git add <file_name>      # Add a specific file
  git add .                # Add all changes
  ```
- **Commit staged changes:**
  ```bash
  git commit -m "Your commit message"
  ```

#### **3. Branching**
- **Create a new branch:**
  ```bash
  git branch <branch_name>
  ```
- **Switch to a branch:**
  ```bash
  git checkout <branch_name>
  ```
- **Create and switch to a branch:**
  ```bash
  git checkout -b <branch_name>
  ```
- **View all branches:**
  ```bash
  git branch
  ```

#### **4. Merging**
- **Merge a branch into the current branch:**
  ```bash
  git merge <branch_name>
  ```
- Resolve conflicts manually if they arise, then stage and commit the resolution.

#### **5. Viewing History**
- **View commit history:**
  ```bash
  git log
  ```
- **View a compact history:**
  ```bash
  git log --oneline
  ```

#### **6. Undoing Changes**
- **Undo changes in a file:**
  ```bash
  git checkout -- <file_name>
  ```
- **Unstage a file:**
  ```bash
  git reset <file_name>
  ```
- **Amend the last commit:**
  ```bash
  git commit --amend -m "Updated commit message"
  ```

---

### **GitHub Integration**

#### **1. Add a Remote Repository**
- **Link your local repo to a GitHub repo:**
  ```bash
  git remote add origin <repository_url>
  ```

#### **2. Push Changes**
- **Push to a remote branch:**
  ```bash
  git push origin <branch_name>
  ```
- **Push the main branch:**
  ```bash
  git push -u origin main
  ```

#### **3. Pull Changes**
- **Fetch and merge changes from a remote branch:**
  ```bash
  git pull origin <branch_name>
  ```

---

### **Working Collaboratively**

#### **1. Forking and Cloning**
- **Fork a repo on GitHub and clone it locally:**
  ```bash
  git clone <your_forked_repo_url>
  ```

#### **2. Creating a Pull Request**
1. Push changes to your branch.
2. Open the original repository on GitHub.
3. Click **Pull Request** > **New Pull Request**.
4. Choose your branch and submit.

#### **3. Resolving Merge Conflicts**
- When conflicts occur:
  1. Open the conflicting file(s).
  2. Resolve conflicts manually.
  3. Stage the resolved file(s):
     ```bash
     git add <file_name>
     ```
  4. Complete the merge:
     ```bash
     git commit
     ```

---

### **Additional Useful Commands**
- **Show changes in files:**
  ```bash
  git diff
  ```
- **Stash changes temporarily:**
  ```bash
  git stash
  ```
- **Apply stashed changes:**
  ```bash
  git stash apply
  ```
- **Delete a branch:**
  ```bash
  git branch -d <branch_name>
  ```
- **Remove a remote:**
  ```bash
  git remote remove origin
  ```


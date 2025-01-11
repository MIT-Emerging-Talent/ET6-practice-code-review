# How to Contribute

Thank you for contributing to **ET6-foundations-group-16**! 🎉 We are excited to
have you on board. This document will guide you through the process of
contributing to the project. Please read through the steps carefully to help us
maintain high-quality code and collaboration. 👩‍💻👨‍💻

## Introduction

This project aims to **improve the quality of software development through peer
code reviews** 📝🔍. We welcome contributions that enhance the code review
process, ensure coding best practices, and help maintain a clean, efficient, and
well-documented codebase. 📚✅ By participating, you help us build a better
repository where developers can share feedback and improve their coding skills
collaboratively. 🤝💡

We believe that a strong code review process is crucial to writing clean,
maintainable code and fostering a collaborative development environment. 💪
Your contribution in enhancing this process, whether through tools,
documentation, or improved review guidelines, is highly valued. 🌟  

## Contribution Guidelines ✨

Before you begin contributing, please review these guidelines to help us
maintain a consistent and high-quality codebase:

- **Fork the Repository** 🍴: Always fork the repository before making changes.
  This ensures that you have a personal copy of the code to work on.
- **Work in Small, Focused Branches** 🌱: Create a new branch for each feature,
  bug fix, or improvement. Name your branch descriptively based on what you're
  working on.
- **Write Clear Commit Messages** ✏️: Make your commit messages concise and
  descriptive. For example, instead of "Fix bug", use "Fix issue with divide by
  zero."
- **Test Your Code** 🧪: Ensure that your code is tested and works as expected.
  If you're adding features, write appropriate tests to verify functionality.
- **Keep Pull Requests Small** 🚀: Focus on one task per pull request. This
  makes it easier to review and reduces the likelihood of conflicts.
- **Respect the Code of Conduct** 🤝: Follow our community's code of conduct
  and behave respectfully in all interactions.

We are committed to maintaining a collaborative and inclusive environment,
and your contribution will play a vital role in the project's success. 🌍💼
With that in mind, let's dive into the steps for contributing! 🏁

---

## Guide to Contributing to the Repository 📚

### Setting Up the Repository and Cloning It

#### Initial Setup Requirements

- Install Git on your local machine (<https://git-scm.com/downloads>)
- Install Visual Studio Code (<https://code.visualstudio.com/>)
- Create a GitHub account if you don't have one

#### Setting Up SSH Keys

1. Open Terminal (Mac/Linux) or Git Bash (Windows)
2. Generate an SSH key:

   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

3. Start the SSH agent:

   ```bash
   eval "$(ssh-agent -s)"
   ```

4. Add your SSH key to the agent:

   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

5. Copy your public key:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

6. Add the key to your GitHub account:
   - Go to GitHub Settings → SSH and GPG keys
   - Click "New SSH key"
   - Paste your public key and save

#### Cloning the Repository Using HTTPS vs. SSH

##### Using SSH (Recommended)

```bash
git clone git@github.com:username/repository.git
```

##### Using HTTPS

```bash
git clone https://github.com/username/repository.git
```

#### Setting Up Your Local Environment

1. Navigate to the project directory:

   ```bash
   cd repository-name
   ```

2. Configure your Git identity:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your_email@example.com"
   ```

3. Open the project in VS Code:

   ```bash
   code .
   ```

#### Making Your First Commit

1. Create or modify a file in your repository
2. Stage your changes:

**For single file change:**

```bash
git add <file name>
```

**For all changes in severals files:**

  ```bash
   git add .
   ```

1. Commit your changes:

   ```bash
   git commit -m "Initial commit: Add project setup files"
   ```

2. Push to the main branch:

For the main branch:

   ```bash
   git push origin main
   ```

For certain branch:

```bash
git push origin <branch_name>
```

#### Troubleshooting Common Setup Issues

- If you encounter permission denied errors, verify your SSH key is properly
  added to GitHub
- For SSL certificate issues, ensure your Git installation is up to date
- If VS Code doesn't recognize Git, restart VS Code after Git installation

---

## 🌟 Creating a Pull Request (PR)

## 🚀 Open a Pull Request

### Navigate to Your Repository

Head over to your forked repository on GitHub, where your code changes are
waiting to shine.

**HOW?**

- Go to your forked repository on GitHub.
- Switch to the branch where you made your changes.

### Compare & Pull Request

Spot the "Compare & pull request" button? Give it a click to start the magic.

**HOW?**

- Select "New Pull Request."
- Compare your branch to the base branch of the original repository.

### Fill Out the PR Template

- 🎨 Title: Craft a catchy yet informative title for your pull request.
- 📝 Description: Paint a picture of your changes. Explain what you did, why it
  matters, and any issues it resolves (e.g., "Fixes #42").
- 🔗 Link Issues: Connect your PR to relevant issues by mentioning them.

### Assign Reviewers

- 🕵️‍♂️ Choose Your Reviewers: Select team members to review your masterpiece.
  This can be done in the right sidebar under "Reviewers."

### Add Labels

- 🏷️ Label It: Use labels to categorize your pull request (e.g., "bug",
  "enhancement", "documentation").

## 🔍 Reviewing a Pull Request

### Check the Code

- 🧐 Inspect the Code: Dive into the code changes. Ensure they follow the
  project's style and guidelines.

### Test the Changes

- 🧪 Experiment: Pull the branch locally and test the changes. Make sure
  everything works like a charm.

### Provide Feedback

- 💬 Comment Constructively: Use inline comments to suggest improvements or
  ask questions. Remember, feedback is a gift!

### Approve or Request Changes

- ✅ Approve: If everything looks great, give it your seal of approval.
- 🔄 Request Changes: If tweaks are needed, request changes and provide clear
  instructions.

## 🔄 Merging a Pull Request

### Ensure All Checks Pass

- ✔️ Check the Checks: Make sure all automated tests and checks are green-lit
  before merging.

### Merge the Pull Request

- 🔗 Seal the Deal: Click the "Merge pull request" button and confirm the merge.
- 🧹 Choose Your Method: Opt for "Squash and merge" for a tidy commit history.

### Delete the Branch

- 🗑️ Clean Up: After merging, delete the branch to keep the repository neat
  and organized.

### Convert to Draft PR

- Click "Convert to draft" when your PR needs more work.
- When Ready for Review: Click "Ready for review" when the PR is complete and
  ready for review.
- Good Draft PR Title: 🔄 [WIP] Add user authentication system

## Good PR Example

- Title: "Add login form validation"
- Changes: 3-5 files
- Lines of Code: ~200 lines
- Feature Focus: Single, focused feature

## Avoid

- Title: "Update entire user system"
- Changes: 20+ files
- Lines of Code: 1000+ lines
- Feature Focus: Multiple features mixed
  
  ---

## ⚠️ Merge Conflict

If you encounter merge conflicts while merging a PR:

1. **Checkout Your Branch**

    ```bash
    git checkout your-branch
    ```

2. **Pull Latest Changes from Main**

    ```bash
    git pull origin main
    ```

3. **Resolve Conflicts**

   Open the conflicting files in your code editor (e.g., VS Code) and manually
   resolve the conflicts.

4. **Stage the Changes**

    ```bash
    git add .
    ```

5. **Commit the Resolution**

    ```bash
    git commit -m "Resolve merge conflicts with main"
    ```

6. **Push the Resolved Changes**

    ```bash
    git push
    ```

After pushing, GitHub will automatically update the PR with the resolved conflicts.

## Best Practices for Collaboration 🤝

Collaboration is key to successful teamwork, and following best practice helps
heep everything running smoothly. Below are some important practices to follow,
complete with examples to ensure effective collaboration:

### Write Commit Messages 📝

Commit messages should clearly describe what changes
have been made and why. A well-written commit message helps other developers
understand the purpose of the change and make it easier to navigate
the project's history.

   **Best Practice for Commit Messages:** ✏️

- **Be clear and concise:** Briefly describe what was changed and why.
- **Follow a consistent format:** This makes it easier to read and understand.
- **Use the imperative mood:** Write messages as commands (e.g "Fix bug"
 instead of "Fixed bug").

 **Examples:**

- **Good Commit Message:**

```bash
  git commit -m "Fix bug in user login validation"
```

  **Explanation:** This message clearly explains that a bug in the
validation has been fixed, which helps others understand the purpose of the change.

- **Bad Commit Message:**

```bash
git commit -m "Fixed login"
```

  **Explanation:** This message is vague and doesn't explain what part of the
login process was fixed or why.
  **Why this important:** Clear commit messages make it easier for your team to
understand changes without needing to dive into the code, and they make reviewing
and tracking changes much easier.

---

### Use Proper Branching Strategies 🌱

Use a structured branching strategy ensures the team works in an organized manner.
Each new task should be worked on in its won branch, which keeps the main
codebase clean and makes collaboration easier.
**Best Practices for Branching:**

- **Create a branch for each task:** Each feature, bug fix, or improvement
should have its own branch.

- **Name branches descriptively:** Use branch names that reflect the task you're
working on.

**Examples:**

- **Feature Branch:**

```bash
git checkout -b feature/login-page
```

**Explanation:** You're creating a branch specifically to work on the login
page feature

- **Bug Fixe Branch:**

```bash
git checkout -b bugfix/fic-header-alignment
```

**Explanation:** This branch is dedicated to fixing an issue with the header alignment.

- **Hotfix Branch:**

```bash
git checkout -b hotfix/fix-crash-on-startup
```

**Explanation:** A hotfix branch is used to add a critical issue, such as a
when starting the application.

**Why this is important:** By creating separate branches for each task and naming
them descriptively, the team can work on multiple tasks at once without interfering
with each other's work. It also makes it easy to track what each branch is
working on.

---

## **Resolving Merge Conflicts 🔧**

Merge conflicts occur when two or more team members changes to the same part of
a file. You need to resolve these conflicts manually to make sure that all
changes are merged correctly.

**Steps for Resolving Merge Conflicts:**

 **Understanding Merge Conflicts** When there's a conflict,
Git will mark the conflicting areas in the file. These markers indicate the
changes made by both you and the other developer.

Imagine two developers are working on the Markdown file ```README.md``` or
python file ```Calculation.py```  for example, in Markdown file:

```Markdown
<<<<<<< HEAD
# How to Contribute  
This guide will help you contributing effectively.

=======
# How to Contribute 

This document explains the best practices for contributing to the project.
>>>>>>> fearuer/section-1
```

In this case, the conflict is in the header(```# How to contribute```), and
both versions contain different text following the heading.

Similarly, in a **Python file**, a conflict could look like this:

```python
<<<<<<< HEAD
def greeting():
    print("Welcome to the project!")
=======
def greeting():
    print("Hello, thanks for contributing!") 
>>>>>>> fearuer/greeting
```

### **How to Resolve Merge Conflicts** 🔧

  **Steps for resolving conflicts in Markdown or Python files:**

- **Step 1: Identify the Conflict** 🕵️‍♂️
- Look for the conflict markers. You will see:
  - ```<<<<<<< HEAD```: The changes you made.
  - ```=======```: The division between your changes and the incoming changes.

  - ```>>>>>>> branch-name```: the changes made by someone else (in the
specified branch)

**Example (Markdown conflict):**

```markdown

<<<<<<< HEAD

# How to Contribute

This guide will help you contribute effectively
=======

# How to Contribute

This document explains the best practices for contributing to the project.
>>>>>>> feature/section-1

```

- **Step 2: Decide which changes to keep** ⚖️

  - You need to decide if you want to keep your changes, the other person’s
changes, or merge both sets of changes.

**In the Markdown file**, you might want to combine both sentences:

```markdown
# How to Contribute

This guide will help you contribute effectively and explains the best practices
for contributing to the project.
```

**In the Python file,** you could keep both greetings or choose one:

```python
def greeting():
    print("Welcome to the project!")
    # Or, combine both greetings:
    # print("Hello, thanks for contributing!")
```

- **Step 3: Remove Conflict Markers** 🧹

  - **After deciding, delete the conflict marker(```<<<<<<```,
```======```, and ```>>>>>>```). For instance, in Markdown:**

```markdown

# How to Contribute

This guide will help you contribute effectively and explains the best practices
for contributing to the project.
```

---
By following these steps, you'll resolve conflicts easily, whether you'er working
on a **Markdown** file or a **Python file**. The key is to understand the
changes, merge them carefully, and test everything before committing your changes.

We are excited to have your contribution to improve the repository and help us
build better software together! 💪

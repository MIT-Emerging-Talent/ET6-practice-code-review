
## Things Explained

### [x] Git  

**What it is:**  
Git is a distributed version control system designed to track changes in code and  
other types of files during software development. It allows users to create multiple  
versions (or "branches") of a project and merge changes seamlessly.

**How it’s used:**  
Developers use Git to clone repositories, commit changes, create branches, and merge  
them back into the main project. It’s a foundational tool for software development  
workflows, especially for collaborative projects.

**Collaboration challenges addressed:**  
Git solves issues including tracking code changes made by several contributors,  
avoiding work loss or overwriting, and keeping track of changes for accountability  
and rollback purposes.

---

### [x] GitHub  

**What it is:**  
GitHub is a cloud-based platform built around Git. It provides hosting for Git  
repositories and offers additional tools for collaboration, project management, and  
code review.

**How it’s used:**  
Teams use GitHub to store their repositories, collaborate on code via pull requests,  
and review or comment on changes. It integrates with other tools for CI/CD, bug  
tracking, and project planning.

**Collaboration challenges it addresses:**  
GitHub simplifies code sharing, collaboration, and integration among distributed  
teams. It provides a centralized place for tracking contributions, reviewing code,  
and merging changes efficiently.

---

### [x] GitHub Repository  

**What it is:**  
A GitHub repository is a storage space for a project on GitHub. It contains all the  
files, commit history, and branches associated with a project.

**How it’s used:**  
Repositories can be public (open to everyone) or private (restricted access). They  
are used to organize project files, track issues, and manage contributions. Users can  
clone repositories to work locally, make changes, and push updates back to the  
repository.

**Collaboration challenges it helps address:**  
GitHub repositories streamline team access to project resources, maintain a clear  
project structure, and ensure that everyone works with the latest version of the  
code.

---

### [x] GitHub Issues  

**What it is:**  
GitHub Issues is a feature for tracking tasks, bugs, and feature requests related to  
a project. It acts as a lightweight project management tool integrated with a  
repository.

**How it’s used:**  
Developers and stakeholders use Issues to document bugs, suggest new features, or  
outline tasks. Each issue can be assigned to team members, labeled, and discussed in  
a comment thread.

**Collaboration challenges it helps address:**  
GitHub Issues helps teams manage project tasks, prioritize work, and improve  
communication. It ensures that all team members are aware of what needs to be done  
and provides a transparent way to track progress.

---

### [x] Pull Requests  

**What it is:**  
A pull request (PR) is a feature in version control systems like Git, often hosted on  
platforms like GitHub, GitLab, or Bitbucket, that allows developers to propose  
changes to a codebase.

**How it’s used:**  
Developers create a pull request after committing changes to a branch. This request  
notifies collaborators that the code is ready for review and integration into the  
main branch. It provides a space for discussing changes, tracking modifications, and  
resolving issues before merging.

**Collaboration challenges addressed:**  
Pull requests help manage contributions by ensuring that all changes are reviewed,  
tested, and agreed upon before integration. They prevent untested or conflicting code  
from being merged, reducing errors and maintaining project stability.

---

### [x] Continuous Integration (CI)  

**What it is:**  
Continuous Integration is a development practice where code changes are  
automatically tested and validated through a series of predefined checks whenever  
changes are pushed to a repository.

**How it’s used:**  
CI systems (e.g., Jenkins, GitHub Actions, CircleCI) automatically run tests, build  
the application, and sometimes even deploy it in staging environments. It ensures  
that new code integrates well with the existing codebase and meets quality standards.

**Collaboration challenges addressed:**  
CI minimizes the risk of introducing bugs or breaking changes by catching issues  
early. It provides instant feedback, enabling teams to work in parallel without fear  
of conflicts or regressions going unnoticed for long periods.

---

### [x] Code Review  

**What it is:**  
Code review is the process of examining written code to identify bugs, enforce  
coding standards, and improve overall quality before merging it into the main  
codebase.

**How it’s used:**  
Teams review code through tools integrated into platforms like GitHub or standalone  
tools like Gerrit. Comments, suggestions, and approvals are shared directly within  
the pull request or codebase.

**Collaboration challenges addressed:**  
Code reviews encourage knowledge sharing, improve code quality, and foster  
collective ownership of the codebase. They help catch mistakes that automated tools  
might miss, ensure alignment with project standards, and improve the skills of all  
contributors.

---

### [x] Project Boards

**What it is:**  
Project boards are visual tools used to organize and manage tasks, often through a  
Kanban-style approach. On platforms like GitHub, project boards are integrated with  
repositories to track issues, pull requests, and overall project progress.

**How it’s used:**  
Teams create columns representing different workflow stages (e.g., “To Do,” “Doing,”  
“Done”). Tasks or issues are represented as cards and move across columns as they  
progress. Labels, deadlines, and assignments can be added to enhance clarity and  
prioritization.

**Collaboration challenges addressed:**  
Project boards provide a clear overview of project status, helping teams stay  
organized and focused. They enhance accountability by assigning tasks to specific  
team members and improve visibility, ensuring everyone understands priorities and  
progress.
m

---


### [x] Project Management Methodologies:  

#### Agile Methodology  
**What it is:**  
Agile is a project management and software development methodology emphasizing  
iterative progress, collaboration, and flexibility. It is designed to adapt to  
changing requirements and deliver value incrementally.

**How it’s used:**  
Teams break projects into smaller, manageable units called iterations or sprints,  
typically lasting two to four weeks. Deliverables are reviewed at the end of each  
sprint, allowing for feedback and adjustments before the next phase. Agile encourages  
regular team meetings (e.g., daily stand-ups) to ensure alignment and quick  
problem-solving.

**Collaboration challenges addressed:**  
Agile promotes transparency, adaptability, and teamwork. It reduces risks associated  
with miscommunication and changing requirements by fostering constant feedback and  
collaboration between team members and stakeholders.

### Waterfall Methodology

**What it is:**  
The Waterfall methodology is a linear and sequential project management approach  
where progress flows in one direction through distinct phases such as requirements  
gathering, design, development, testing, and deployment.

**How it’s used:**  
Teams complete each phase entirely before moving to the next. Detailed documentation  
is created upfront, and the scope of the project is fixed early in the process. This  
methodology is best suited for projects with well-defined requirements that are  
unlikely to change.

**Collaboration challenges addressed:**  
Waterfall provides a clear structure and timeline, ensuring all stakeholders know  
what to expect at each stage. It reduces ambiguity by requiring thorough  
documentation and planning, making it easier for large teams to coordinate their  
efforts.

---

### Scrum Methodology

**What it is:**  
Scrum is a subset of Agile, focusing on delivering high-value increments of work in  
short, time-boxed iterations called sprints. It is centered around roles (e.g.,  
Scrum Master, Product Owner, Team), events (e.g., sprint planning, daily stand-ups),  
and artifacts (e.g., product backlog, sprint backlog).

**How it’s used:**  
Teams work in sprints (usually 2–4 weeks) to deliver a potentially shippable product  
increment. A Scrum Master ensures the process runs smoothly, while the Product Owner  
prioritizes tasks in the backlog. Continuous feedback from stakeholders drives  
improvements in subsequent sprints.

**Collaboration challenges addressed:**  
Scrum improves team alignment through daily stand-ups and retrospective meetings. It  
enhances productivity by breaking down tasks into smaller, manageable chunks and  
ensures frequent communication between team members and stakeholders.

---

### Kanban Methodology

**What it is:**  
Kanban is a visual project management approach designed to improve workflow and  
reduce inefficiencies. It emphasizes continuous delivery without overloading the  
team.

**How it’s used:**  
Teams use a Kanban board with columns representing workflow stages (e.g., “To Do,”  
“In Progress,” “Completed”). Tasks or work items are visualized as cards that move  
across the board as they progress. Work-in-progress (WIP) limits are set to ensure  
the team focuses on a manageable number of tasks.

**Collaboration challenges addressed:**  
Kanban fosters transparency and flexibility, allowing teams to identify bottlenecks  
and optimize workflows in real-time. It enhances accountability and ensures that  
work is distributed evenly across team members.

---

### Lean Methodology

**What it is:**  
Lean methodology focuses on maximizing value and minimizing waste in project  
workflows. Originally developed for manufacturing, it has been adapted for software  
development and project management.

**How it’s used:**  
Teams identify value streams and eliminate non-essential processes to ensure a  
smooth and efficient workflow. Continuous feedback loops and a focus on delivering  
customer value drive decision-making. Lean incorporates tools like value stream  
mapping, just-in-time production, and root cause analysis.

**Collaboration challenges addressed:**  
Lean promotes efficiency by streamlining workflows and focusing on what truly  
matters. It enhances team collaboration by encouraging cross-functional participation  
and regular feedback, ensuring that everyone contributes to delivering value.

---

### Hybrid Methodology

**What it is:**  
The Hybrid methodology combines elements of Agile and Waterfall to leverage the  
strengths of both approaches. It provides structure for well-defined phases while  
allowing flexibility and iteration in areas prone to change.

**How it’s used:**  
Teams use Waterfall for fixed and predictable project phases (e.g., requirements  
gathering, design) and Agile for phases requiring iterative development and frequent  
stakeholder input (e.g., development, testing).

**Collaboration challenges addressed:**  
Hybrid methodology allows teams to balance planning and adaptability. It enhances  
communication and alignment by using the structured approach of Waterfall for  
clarity while maintaining the flexibility of Agile to respond to evolving needs.

---

### Command Line Interface / Terminal

**What it is:**  
The Command Line Interface (CLI) is a text-based interface used to interact with a  
computer’s operating system or software applications. It allows users to execute  
commands by typing them, rather than using a graphical interface.

**How it’s used:**  
Developers use the CLI to navigate file systems, execute scripts, and manage tools  
like Git. For instance, commands like `git clone`, `git commit`, and `git push` allow  
users to manage version control directly from the terminal. The CLI is also essential  
for configuring environments, automating tasks, and accessing server systems.

**Collaboration challenges addressed:**  
The CLI enables efficient and precise execution of tasks, reducing dependency on  
graphical tools. This consistency in commands and workflows ensures all team members  
can replicate processes, troubleshoot effectively, and work seamlessly across  
environments.

---

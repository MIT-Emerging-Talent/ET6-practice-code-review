# Things Explained
## Project Methodologies
### Saliha

#### What is it?
Project methodologies are structured frameworks that help teams plan, execute, and deliver projects effectively. They define processes, roles, and workflows to ensure clarity and coordination. Common examples include:
- **Agile**: Focuses on iterative and incremental work cycles with frequent feedback and flexibility.
- **Scrum**: A subset of Agile that organizes work into time-boxed sprints with specific goals.
- **Waterfall**: A linear approach where each project phase (e.g., planning, execution) is completed sequentially.

#### How is it used?
Teams implement these methodologies to create order and predictability in project workflows. For example:
- **Agile**: Promotes adaptability through daily stand-ups, iterative reviews, and continuous feedback.
- **Scrum**: Breaks the project into short sprints, each with a deliverable outcome and regular reviews.
- **Waterfall**: Follows a predefined sequence, ideal for projects with clear and unchanging requirements.

By adopting these methodologies, teams set milestones, prioritize tasks, and maintain collaboration throughout the project lifecycle.

#### Which collaboration challenges does it help address?
- **Shared Understanding**: Clearly defines roles, responsibilities, and goals to ensure everyone is aligned.
- **Task Division**: Breaks down complex projects into manageable pieces, making individual contributions clear and achievable.
- **Task Tracking**: Uses tools like backlogs, sprint boards, and milestones to monitor progress and address issues early.

## Command Line Interface / Terminal
### Saliha

#### What is it?
A CLI is a text-based interface that allows users to interact with the computer's operating system by typing commands. The terminal is the environment where these commands are executed.

#### How is it used?
Developers use the CLI to perform tasks such as navigating directories, managing files, and interacting with version control systems like Git. For example, `git status` checks the current repository status. 

Developers use the CLI to perform a wide range of tasks, such as:
- **Navigating directories** (`cd`, `ls` commands).
- **Managing files** (`mkdir`, `rm` commands).
- **Interacting with version control systems like Git** (`git status`, `git commit`).
- **Running scripts and automating repetitive tasks**.

The CLI is favored for its speed, precision, and ability to chain commands for complex operations.

#### Which collaboration challenges does it help address?
- **Task Division**: Allows team members to execute specific tasks efficiently without reliance on graphical tools, promoting clarity and precision.
- **Reassembling**: Simplifies version control and enables seamless merging of contributions using tools like Git.
- **Consistency**: Ensures uniform workflows across platforms, reducing misunderstandings and errors.

The CLI’s flexibility and power make it an essential tool for collaborative development, enabling efficient task management and integration.

## Git
### Mohammad

#### What is it?
Git is a distributed version control system that tracks code changes and allows multiple developers to collaborate efficiently. It ensures every team member has a complete copy of the project, including its history, enabling both online and offline work.

#### How is it used?
Git is a tool that helps developers manage their code and work together more easily on projects. It keeps track of every change made to the code, so developers can save their progress (commits), share updates with their team (push/pull), and create separate branches to work on new features or fixes without interfering with others’ work.

#### Which collaboration challenges does it help address?
Git addresses several collaboration challenges, such as:
- **Conflicting changes** when multiple developers edit the same files.
- **Tracking changes** to understand who made updates and why.
- **Ensuring everyone works on the latest version** of the project.

It also allows parallel work on separate branches, resolves conflicts during merges, and improves communication through commit messages and pull requests. Additionally, Git provides accountability and transparency by maintaining detailed version history and a clear record of contributions. By solving these challenges, Git streamlines collaboration, enhances team productivity, and minimizes the risks of errors in software development.

## GitHub
### Rumiya

#### What is it?
GitHub is a software repository hosting platform where developers come together to store, manage, and contribute to their own and others' projects. The platform facilitates the interaction of people who can view, contribute, and share each other’s work.

Having started as a developer’s collaborative platform, GitHub is now the most significant cloud-based storage space for software projects that exist on the planet.

#### How is it used?
GitHub allows programmers to duplicate code from a project and safely work on it without changing the code within the original project. Once the additional code is written, reviewed, and contains no breaking changes, the code can be merged with the source code, thus contributing to the source code. The collaborations on GitHub can be private and public.

#### Which collaboration challenges does it help address?
- **Version Control**: GitHub provides a robust version control system, Git, allowing teams to track changes, revert to previous versions, and avoid overwriting each other's work.
- **Collaboration and Coordination**: It enables multiple contributors to work on the same project simultaneously without conflict. Branching and merging allow teams to manage contributions efficiently.
- **Code Integration**: Pull requests and code reviews facilitate seamless code integration, helping teams catch errors or bugs early and maintain high code quality.

## GitHub repository
### Meklit
A GitHub repository is a place to share code, files, and version history. It allows multiple people to work on the project simultaneously, allowing different parts of code to merge smoothly. When overlap happens, it allows for merging conflicts that the team must resolve manually, making collaboration easier.

## GitHub Issues
### Mohammad
GitHub Issues is a tool for tracking tasks, bugs, and feature requests in projects. Teams can create issues, organize them with labels and deadlines, and assign them to members for better task management. Each issue includes a discussion area where team members can collaborate and solve problems together. Issues can also be linked to pull requests, making it easy to track related code changes. GitHub Issues helps improve communication, ensure transparency, and keep teams aligned on goals. It also integrates with other tools to streamline workflows and increase productivity.

## Project Boards
### Anna
A project board is a visual tool used to manage tasks, track progress, and collaborate effectively in team projects. It typically organizes work into columns, representing different stages of a workflow, such as “To Do,” “Doing,” “In review,” and “Reviewed.” Each task or deliverable is represented as a card that can be moved across columns as the work progresses.

#### How is it used?
- **Task Management**: Break down projects into smaller, actionable tasks.
- **Progress Tracking**: Monitor the status of tasks in real-time by observing the movement of cards.
- **Prioritization**: Assign priorities, deadlines, or tags to tasks for better focus.
- **Collaboration**: Allow team members to contribute updates, add comments, and attach resources directly to the cards.

#### Challenges it helps address:
- **Lack of Visibility**: Ensures everyone knows the project's current status and priorities.
- **Inefficient Communication**: Centralizes task-related discussions and reduces the need for endless email chains.
- **Role Confusion**: Clarifies responsibilities by assigning tasks to specific team members.
- **Missed Deadlines**: Encourages accountability with deadlines and progress indicators.

## Pull Request
### Anna's Version
A pull request in GitHub is a feature used to propose changes to a repository. It allows developers to review, discuss, and merge code changes into the main branch. Contributors submit their updates via pull requests, enabling collaboration, code review, and feedback before the changes are approved and integrated.

#### To submit a pull request on GitHub:
1. **Fork and Clone**: Fork the repository, then clone it to your local machine.
2. **Create a Branch**: Create a new branch for your changes (e.g., `git checkout -b feature-branch`).
3. **Make Changes**: Edit files and commit your changes (`git commit -m "Your message"`).
4. **Push Changes**: Push the branch to your fork (`git push origin feature-branch`).
5. **Open a Pull Request**:
   - Go to the original repository on GitHub.
   - Click "Pull Requests" > "New Pull Request".
   - Select your branch and add a title/description.
6. **Submit**: Click "Create Pull Request" to submit it for review.

## Continuous Integration (CI)
### Mushtary
Continuous Integration (CI) is a practice in software development where code changes from multiple developers are automatically merged, tested, and validated frequently, usually several times a day.
- Developers work on small parts of the code.
- They upload (or "integrate") their changes into a shared codebase regularly.
- Automated tools check the code to make sure it works and doesn't break anything.

## Code Review
### Anna's Version
Code review is a collaborative process where team members examine code changes to ensure quality, functionality, and alignment with project standards before merging into the main branch.

#### How is it used?
- **Pull Requests**: Review changes submitted via pull requests in platforms like GitHub.
- **Feedback**: Provide comments, suggestions, and approve or request modifications.
- **Standards Enforcement**: Verify adherence to coding standards and best practices.

#### Collaboration Challenges it solves:
- **Quality Assurance**: Identifies bugs or inefficiencies early.
- **Knowledge Sharing**: Helps team members understand the codebase and improve skills.
- **Accountability**: Encourages responsibility for code quality.
- **Consistency**: Maintains uniform coding styles and practices across the team.

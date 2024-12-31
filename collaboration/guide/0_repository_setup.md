# Repository Setup

Before diving into your project, make sure your team has all the practical things in place. This step isn't very hard, but everything will go more smoothly if you take the time to do this correctly at the beginning.

## Setup and Share a Repository

As a team, you will choose the name for your team and select someone from your team to be the repo owner. This person will fork this repository and configure it for collaboration:

- Public face of your repository:
    - Change your repository description 
      (https://stackoverflow.com/questions/7757751/how-do-you-change-a-repository-description-on-github)
    - Add or remove topics from your repository
    - Update your main README with your group name 
      and an initial overview. 
      (You can change this as much as you want.)
- Under settings in your repository select:
    - Issues
    - Projects
    - Always suggest updating pull request branches
- Collaboration Settings:
    - Require a code review for PRs to `main`/`master`
      ([owanateamachree](https://owanateamachree.medium.com/how-to-protect-the-master-branch-on-github-ab85e9b6b03),
      [GitHub docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/approving-a-pull-request-with-required-reviews))
      - You will need to type `master` into the 
        Branch name pattern input box 
        (or type `main` if you have changed your default branch).
  - Select these settings to protect matching branches:
      - Require approvals
      - Dismiss stale pull request approvals 
        when new commits are pushed
      - Require approval of the most recent reviewable push
      - Require conversation resolution before merging
      - Do not allow bypassing the above settings

## README

Write the main README ([../../README.md](../../README.md)) 
for your repository! 
You can always update it as you learn more about code review 
and collaboration on GitHub.

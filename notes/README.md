# Notes
## How to Create a Branch

Branches are essential to work on new features, bug fixes,
 or experiments without affecting the main codebase. Here's how you can create
 a branch:

1. **Navigate to your repository:** Go to the main repository on GitHub.
2. **Create a new branch:** In your local repository,
 use the command `git checkout -b <branch-name>` to create and switch to a new branch.
3. **Push the branch to GitHub:** After making your changes,
 push your branch to the remote repository using `git push origin <branch-name>`.
4. **Create a Pull Request (PR):** After pushing the branch,
 go to GitHub, and create a PR to merge your changes.

For more detailed information, refer to the official GitHub documentation on
For more detailed information, refer to the official GitHub documentation on
[Creating and Deleting Branches Within Your Repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository).

---
## How to Create a Pull Request

A Pull Request (PR) allows you to propose changes to the codebase.
 Here's a general guide on how to create a pull request:

1. **Fork the repository (if necessary):** If you are working on a forked repository,
 ensure you have your own copy of the repository.
2. **Create a branch:** Start by creating a new branch to work on your feature
or bug fix. This ensures that your changes are isolated.
3. **Make your changes:** Modify the codebase as needed, ensuring to commit your
 changes with meaningful messages.
4. **Push your changes:** Push your branch to the remote repository once you're
 satisfied with your changes.
5. **Open a Pull Request:** Go to the repository's "Pull Requests" tab on GitHub
 and click the "New Pull Request" button. Select your branch and the base branch
 you want to merge into (usually `main` or `master`).
6. **Provide a description:** Describe what changes you made, why you made them,
 and any additional context that may help the reviewers.
7. **Request a review:** Assign team members to review your PR and wait for
 their feedback.
8. **Merge the PR:** After the review is complete, and if no conflicts exist,
 the PR can be merged into the main codebase.

For more detailed information, refer to the official GitHub documentation on
 [Creating a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

 ---

## How to Review a Pull Request

Reviewing a pull request (PR) is an essential part of the collaborative process,
 ensuring code quality and consistency. Here's how to review a PR:

1. **Access the PR:** Go to the "Pull Requests" tab in the repository and
 click on the PR you want to review.
2. **Understand the changes:** Read through the description provided by the author
 and check the files changed tab to see the proposed changes.
3. **Review the code:** Look through the code changes, ensuring it aligns with
 the coding standards, functionality, and overall project goals. You can
add comments or suggest changes.
4. **Test the changes (if applicable):** If necessary, pull the branch and test
 the code locally to ensure everything works as expected.
5. **Leave Feedback:** You can leave comments or approve the PR directly.
 If there are issues or improvements to be made, request changes
  or leave comments for clarification.
6. **Approve or Request Changes:** Once you've reviewed the PR, you can either
 approve it or request changes. If you're satisfied, approve it.
  If something needs attention, request the necessary changes.

For more detailed information, refer to the official GitHub documentation on
 [Reviewing Proposed Changes in a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request).

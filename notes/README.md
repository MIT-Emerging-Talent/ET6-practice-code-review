# Notes
<!--
  Notes:
  - Document bugs encountered during the project and their solutions.
  - Include details such as error messages, causes, and fixes.
  - Keep explanations clear and focused on troubleshooting.
  - Ensure the steps provided can be easily followed for similar issues in the future.
-->

## Import Method

In our project, we use both relative and absolute import methods to include
modules and functions from different files. Here are the key points:

- **Relative Imports**: These are used to import modules relative to the current
  module's location. For example:

python
  from ..repeat_character import repeat_character

- **Absolute Imports**: These are used to import modules using the full path
 from the project's root directory. For example:

python
  from solutions.repeat_character import repeat_character

---

## Issues Faced

### 1. Import Errors

- **Error:** Unable to import solutions.repeat_character.
- **Cause:** This error occurred due to incorrect relative import paths. The
module could not be found because the path was not correctly specified relative
to the current file's location.
- **Solution:** We resolved this by using both relative and absolute imports and
ensuring the correct project structure. This allowed us to pass the checks.  
  [Workflow](https://github.com/MIT-Emerging-Talent/ET6-foundations-group-06/blob/main/.github/workflows/ci-checks.yml)

- **Test Failures:**
  - **Observation:** All the code seems correct and should work, but tests are
failing in one file while pointing to another.
  - **Possible Cause:** We've noticed that others have also reported some bugs
and strange behavior on GitHub, so it could be an issue on their side.

---

### 2. Conflict Error in Checklist

- **Error:** Conflict detected in a file that does not exist in the current branch.
- **Cause:** The file shown to have a conflict does not exist in the current branch.
- **Solution:** Evan suggested leaving a comment and not worrying about it, as it
does not affect the current branch.

---

### 3. Formatting Error in checklist.yml

- **Error:** Formatting errors detected by ruff in a file.
- **Cause:** The issue was due to an outdated ruff version and incorrect
formatting in the file.
- **Solution:** We resolved this by updating ruff to the latest version and
fixing the formatting in the file. This solved the issue.

---

### 4. Formatting Errors in Multiple Branches

- **Cause:** These branches were created when the main branch contained bugs.
- **Solution:** Merge the updated, bug-free main branch into the affected branches
to resolve the errors.

---

- By documenting these issues and solutions, we can ensure better understanding
and troubleshooting for future in development.

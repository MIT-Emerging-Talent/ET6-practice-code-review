<!-- this template is for inspiration, feel free to change it however you like! -->

# Constraints

Some boundaries around our project are here now live.

## External

<!--
  constraints coming from the outside that your team has no control over:
  - projects deadlines  
  - number of unit tests required to pass a code review
  - technologies (sometimes a client will tell you what to use)
  - power or connectivity
  - ...
-->

**1. Deadline:** Ensure the project is completed and tested before 10th/Jan/2025.

**2. Code Review:** The code must pass at least 4 unit tests to be considered complete.

**3. Libraries:** Use only standard Python libraries and `pytest` for testing.

**4. Version Control:** Use Git and GitHub for collaboration. Main branch
 protection enabled.

**5. Packaging:** Ensure the module is packaged for installation using `setup.py`.

## Internal: Involuntary

<!--
  constraints that come from within your team, and you have no control over:
  - each of your individual skill levels
  - amount of time available to work on the project
  - Most members are inactive on slack
-->

**1. Daily Time Commitment:** Each team member commits at least 2 hours per day
 to work on his/her own project.

**2. Hardware:** All team members must use devices capable of running
 Python 3.10.0 or higher.

## Internal: Voluntary

<!--
  constraints that your team decided on to help scope the project. they may include:
  - coding style & conventions
  - agree on a code review checklist for the project repository
  - the number of hours you want to spend working
  - only using the colors black and white
-->

**1. Language and Frameworks:**

- Use Python (minimum version 3.10.0).
  
  **(a). Naming Conventions:**
  
- File names must be in lowercase and use underscores (e.g., `good_fruit_names.py`).
  
- Testing files must follow the naming pattern `test_<module_name>.py` (e.g., `test_good_fruit_names.py`).
  
  **(b). Collaboration Tools:**

- Use GitHub Issues and Projects for task tracking.

- Use Slack for communication.

**2. Team Roles:**

  **(a). Developer:** Writes the main logic for the module.

  **(b). Tester:** Develops unit tests and ensures code coverage.

  **(c). Documenter:** Prepares project documentation, including a README.md file.

  **(d). Reviewer:** Reviews pull requests before merging to the main branch.

**3. Scope of the Module:**

- Input: A name (string).

- Output: Boolean value indicating if the name contains consecutive identical letters.

- Edge cases: Handle special characters, empty strings, and numeric values gracefully.

**4. Documentation:**

- Include a README file with clear instructions on usage.

- Provide example input and output.

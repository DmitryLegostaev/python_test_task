# AQA Engineer test task

Introduction
The test task for the position of Automation QA Engineer consists of 3 parts and is designed to
test the key professional knowledge and skills for this position. Please, use Python
programming language to make it.

### UI test

Please create a UI test:

Steps:

1. Open https://qa.awarasleep.com/ -> check the page is opened
2. Click the “Shop & Save” button on the Hero Banner -> check you are on /mattress
3. Add the mattress to the cart -> Check the mattress has been added to the cart

### API test

Create a API test with CRUD operations around the User flow using the following Portal:
https://reqres.in/

Steps:

1. Create a User
2. Get Single User by ID (already existing #12)
3. Update user by Patch method
4. Update user by Put method
5. DELETE User by ID (already existing #12)

For each step make a response status and response body checks. It is a fake API and the data
will not be added in reality. That means you can’t check Add User -> Get User By ID.

### Additional tasks
1. Create a Repository on GitHub and allocate the testing code there.
2. Provide instructions on how to execute tests (please include README.md file).
3. Provide a simple tool to review results (Allure, etc)
4. CI/CD the automation in CircleCI. Run tests on each commit. Uploading the test artifacts
   would be a plus.

# Repo overview
## Notes
1. There is a requirement in the task to use CircleCI as CI/CD tool, however, as been discussed during the interview, usage of CircleCI is not a strict requirement, so I decided to choose GitHub Workflows for this task by multiple reasons.
2. Some brief "how-to" run and publish the results on local pc is added, but details are missing intentionally, as the expected way to run tests is by CI/CD.
3. "pylenium" is chosen as a selenium wrapper in UI tests to simplify common automation actions during selenium usage. It requires to conftest.py auto-generated stored in root of the repo. These files contain some pep8 issues, and they are excluded from a flake8 lint.
4. "main" branch of the repo is protected by approvals and checks.
5. There are two different allure step types for UI and API test, and test-specific steps from the UI test could be reworked similar to API test steps to provide better re-usability.
6. There are no guidelines and rules specified for steps naming, but they could be added in the real project.

## Manual usage
### How to run the tests:
1. Download the repo
2. Create new python virtual environment (recommended to use Python 3.9 or higher)
3. Install packages listed in the requirements.txt file
4. Make sure browser specified in pylenium.json is installed in your system
5. Run pytest from root of the project using the environment created in previous steps

### How to generate and view allure report (Windows)
1. Include the following arguments to a pytest run (point 4 from previous list) "--alluredir=./allure-results"
2. Make sure Java is installed and JAVA_HOME added to env vars
3. Download allure zip from official website
4. Unzip it
5. From the root of the project run allure.bat serve command. Make sure it is collecting "allure-results" dir

## Workflow on GitHub
1. Current report with trends and history available here https://dmitrylegostaev.github.io/python_test_task
2. Currently, the same report is used for tests for all branches
3. Max reports count = 20
4. Reports is located on gh-pages branch
5. All workflow runs could be found here https://github.com/DmitryLegostaev/python_test_task/actions

### Usage:
1. Push a commit to any branch
2. First GitHub workflow job will lint and test the code, upload the allure results as artifact to GitHub storage
3. Second GitHub workflow job will download the latest allure results, download history, generate report and publish it to GitHub Pages

### Known limitations: 
1. GitHub pages publishing could take up to 10 mins to display the results
2. Need to change the approach to store different trends for different branches
3. The workflow is designed to run on a single python package and needs changes in order to provide readable cross-package test results
4. Once GitHub monthly quota for CI/CD agents usage is reached, need to set up and spin local agents, and make some changes to workflow file to use these local agents
5. Probably, the repo report should not exceed the GitHub Pages limits, however, need to keep the limits in mind if the project(real project) will expand in the future
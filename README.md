# AQA Engineer test task

Introduction
The test task for the position of Automation QA Engineer consists of 3 parts and is designed to
test the key professional knowledge and skills for this position. Please, use Python
programming language to make it.

# UI test

Please create a UI test:

Steps:

1. Open https://qa.awarasleep.com/ -> check the page is opened
2. Click the “Shop & Save” button on the Hero Banner -> check you are on /mattress
3. Add the mattress to the cart -> Check the mattress has been added to the cart

# API test

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

# Additional tasks

1. Create a Repository on GitHub and allocate the testing code there.
2. Provide instructions on how to execute tests (please include README.md file).
3. Provide a simple tool to review results (Allure, etc)
4. CI/CD the automation in CircleCI. Run tests on each commit. Uploading the test artifacts
   would be a plus.

# How to run the tests:

1. Download the repo
2. Create new python virtual environment (recommended to use Python 3.9 or higher)
3. Install packages listed in the requirements.txt file
4. Run pytest from root of the project using the environment created in previous steps

# How to generate and view allure report (Windows)

1. Include the following arguments to a pytest run (point 4 from previous list) "--alluredir=./allure-results"
2. Make sure Java is installed and JAVA_HOME added to env vars
3. Download allure zip from official website
4. Unzip it
5. From root of the project run allure.bat with full path specified
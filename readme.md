# <img src="/static/img/readme/logo.png" alt="Nutrition Self-management Platform" width="30px"/> Nutrition Self-management Platform

Nutrition Self-management Platform shows users personalized nutrition information based on a 12-item screener. The screener includes a progress tracking feature, allowing users to stop and resume anytime. Users are assigned up to 4 learning modules based on criteria that correspond to dietary recommendations. Each module consists of theme-based nutrition information and a quiz that checks for understanding. Quizzes include fill-in-the-blanks, matching, sorting and select-all-correct. The platform can be easily adapted to different settings that require screening, task assignment and knowledge checking.

![Nutrition Self-management Platform](/static/img/readme/homepage.png "Homepage")

**Contents**
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Future Features](#future-features)
- [Installation](#installation)
- [Demo](#demo)
- [About the Developer](#about-the-developer)

## Tech Stack

**Backend:** Python, PostgreSQL, Flask, SQLAlchemy, Jinja

**Frontend:** JavaScript, HTML, CSS, Bootstrap, React

## Features

**The 12-item nutrition screener**

After creating an account, users are guided through the screener. Backend algorithms ensure that users are only shown relevant questions and check inputs inputs before they are submitted to the database.

<img src="/static/img/readme/screener.gif" alt="Screener" width="500px"/>

**Screener progress tracking**

Through keeping a progress tracker in the Postgres database and updating it each time users move on to a new question, users are able to leave anytime and resume the screener at the right question.

<img src="/static/img/readme/progress.gif" alt="Progress Tracking" width="500px"/>

**Module assignment**

After completion of the screener, users are assigned modules based on cut-offs that correspond to dietary recommendations. Each module has a quiz at the end to check for understanding.

<img src="/static/img/readme/modules.gif" alt="Modules" width="500px"/>

**Unlimited quiz attempts**

Quizzes are built using a mix of plain javascript and React. With the use of AJAX requests, users can check answers and retry without reloading the page.

<img src="/static/img/readme/ajax.gif" alt="Ajax" width="500px"/>

**Enhanced interactivity**

Some quizzes use the drag and drop HTML feature, making them easy for users to navigate.

<img src="/static/img/readme/dragndrop.gif" alt="Drag and Drop" width="500px"/>

Quiz built with React gives immediate feedback when users make a selection, giving users quick visual feedback.

<img src="/static/img/readme/react.gif" alt="React" width="500px"/>

## Future Features

- Display of screener result as a nutrition report 
- Quiz progress tracking
- Service provider interface

## Installation

**Prerequisites**

To run the Nutrition Self-management Platform, you will need to have Python 3 and PostgreSQL installed on your machine.

**Running the Nutrition Self-management Platform on your machine**

Clone this repository
```shell
git clone https://github.com/juliatangwc/hb-project-nutrition-self-management-platform.git
```
Optional: Create and activate a virtual environment using virtualenv
```shell
pip3 install virtualenv
virtualenv env
source env/bin/activate
```
Install dependencies from requirements.txt
```shell
pip3 install -r requirements.txt
```
Create your database & seed sample data
```shell
createdb diet-screener
python3 seed_database.py
```
Run the app on localhost
```shell
python3 server.py
```
## Demo
[Click here](https://www.youtube.com/watch?v=Ql86x3UN-JQ) to watch the demo.

## About the Developer
Julia is a naturally curious person who enjoys problem-solving and learning new things along the way. She started a career in research upon graduating as a registered dietitian. For the past 6 years, she led research projects to develop dietetic service for the first cancer care center in Hong Kong and obtained a PhD in public health in the process. During that time, her research projects on health reminders and facilitative e-tasks in nutrition counseling introduced her to the exciting world of software engineering. She was inspired by how technology is changing every aspect of our lives and aspired to be part of the change. She is excited to be graduating from Hackbright Academy and to start making a positive impact with her skills.

[![LinkedIn][LinkedInImg]][LinkedInLink]

[LinkedInImg]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[LinkedInLink]: https://www.linkedin.com/in/juliatangwc
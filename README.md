# Medical Triage Expert System

This project implements a medical triage expert system designed to assist hospital staff in prioritizing patients based on their medical conditions.  The system uses a rule-based approach to assess patient symptoms and assign a priority level.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

## Introduction

In a busy emergency room or during a mass casualty event, rapid and accurate triage is crucial. This system aims to streamline this process by using a knowledge base of medical rules.  It takes patient symptoms as input and infers a priority level (e.g., Critical, High, Medium, Low) and a corresponding message indicating recommended action.

## Features

* **Symptom Input:**  Users can input patient symptoms in a comma-separated format.
* **Rule-Based Inference:** The system uses a knowledge base of medical rules to determine priority.
* **Priority Assignment:**  Assigns a priority level based on matching symptoms to rules.
* **Clear Output:** Provides the assigned priority level and a descriptive message.
* **Database Storage:** Medical rules are stored in a MySQL database.
* **Graphical User Interface (GUI):** A GUI is provided for user interaction (currently using Tkinter, planned migration to PyQt or Kivy).

## Requirements

* **Python 3.x**
* **Flask**
* **SQLAlchemy**
* **MySQL Connector**
* **Tkinter**
* **Ttbootstrap**
* **python-dotenv**

You can install the Python dependencies using:

```bash
pip install Flask SQLAlchemy mysql-connector-python python-dotenv tk ttbootstrap
```

## Installation
- Clone the repository:

```bash

git clone https://github.com/rhoda-lee/medical-triage.git
```

- Create a virtual environment
```bash
python3 -m venv myenv
source ~/myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

- Install the dependencies 
    - See Requirements

- Create a .env file in the project root and add your database credentials
```bash
DB_USERNAME=your_db_username
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
```

## Usage
- Database Setup: 
Follow the instructions in the Database Setup section - [Database Setup Section](#database-setup)

- Run the Flask app:
```bash
python3 app.py
```
- Run the GUI (if using the Tkinter version)
```bash
python3 gui.py
```
- Access the API endpoints (e.g., /classify) if you're not using the GUI

## Database Setup
Create a MySQL database with the name specified in your .env file (DB_NAME)

- Run the models.py script to create the necessary tables
```bash
python3 models.py
# This will create the rules table in your database
# Make sure your database credentials are correctly set up in the .env file
```

> Populate the rules table with your medical rules. You can do this manually using a MySQL client or by writing a script to insert the data. The rules table has conditions, priority and message columns

## Project Structure
medical-triage/ <br>
├── app.py     <br>
├── gui.py     <br>
├── models.py  <br>
├── config.py  <br>
├── rules_crud.py <br>
├── .env          <br>
└── README.md 


## Future Improvements
- Enhanced GUI: Migrate to PyQt or Kivy for a more modern and user-friendly interface
- More Sophisticated Inference Engine: Explore using a more advanced inference engine
- Symptom Checker: Implement a symptom checker with a predefined list of symptoms
- User Authentication: Add user authentication
- Integration with Hospital Systems: Integrate with existing hospital information systems
- Machine Learning Integration: Explore using machine learning to improve accuracy

## License
[MIT LICENSE](/LICENSE)

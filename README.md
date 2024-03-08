# Time Sheet Autofill ⏰💩

## Description

This script automates the process of filling the time sheet form. It reads data from a JSON file and fills the form accordingly.

## Requirements

- Python 3.x
- Chrome browser installed
- Required Python packages: `selenium`

## Installation

1. Install Python 3.x from [Python.org](https://www.python.org/downloads/).
2. Install Chromedriver from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).
3. Install required Python packages using pip:

    ```
    pip install selenium
    ```

## How to Run

1. Clone or download the repository to your local machine.
2. Navigate to the directory contai(5)dataning the script.
4. Modify the environment variables in the `.env` file according to your credentials.

    ```
    USERNAME=your_username
    PASSWORD=your_password
    ```

5. Modify the data in the `time.json` file to specify working hours by project.

6. Run the script using Python:

    ```
    python script.py
    ```

## Environment File (.env)

The `.env` file contains sensitive information like login credentials. Make sure to keep this file secure and do not share it publicly. Modify the values of `USERNAME` and `PASSWORD` to match your login credentials.

## JSON File (time.json)

The `time.json` file contains the data used to fill the form. Each object in the JSON array represents a set of data for filling the form. Modify the values to specify the working hours for each project.

Example JSON format:

```json
[
    {
        "projet": "Project A",
        "tache": "Task 1",
        "type": "Type 1",
        "lundi": "Value for Monday",
        "mardi": "Value for Tuesday",
        "mercredi": "Value for Wednesday",
        "jeudi": "Value for Thursday",
        "vendredi": "Value for Friday",
        "samedi": "Value for Saturday",
        "dimanche": "Value for Sunday"
    },
    {
        "projet": "Project B",
        "tache": "Task 2",
        "type": "Type 2",
        "lundi": "Value for Monday 2",
        "mardi": "Value for Tuesday 2",
        "mercredi": "Value for Wednesday 2",
        "jeudi": "Value for Thursday 2",
        "vendredi": "Value for Friday 2",
        "samedi": "Value for Saturday 2",
        "dimanche": "Value for Sunday 2"
    }
]

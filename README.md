# Backend Engineering Challenge

## Overview:

The challenge revolves around processing a stream of translation events and calculating a moving average of translation delivery time over a specified window size.

The application accepts JSON-formatted input, processes it, and generates a sequence of 1-minute interval timestamps accompanied by the corresponding delivery time averages, presented in the form of a dictionary. 

To ensure accuracy and proper functioning, certain assumptions were made regarding the structure and order of the input data:

- The input file had a valid JSON structure;
- The timestamp field structure was a string consistent with the input example;
- The lines are sorted from oldest to newest.

## Setup Instructions

The application has minimal dependencies, the only one being **Pytest 7.1.1**. It was developed using **Python 3.10**. To prepare for running the command-line interface (CLI), install the program dependencies with the following command:

```pip install -e . ```
## How to Run the Application

Open a terminal and use the following command:

```moving_average -i events.json -w 10 ```

Here, **-i** specifies the input JSON file, and **-w** defines the moving average window size in minutes.

The application offers the following command-line parameters:
```
usage: moving_average [-h] -i INPUT_FILE [-w WINDOW_SIZE]

Moving average delivery times

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        Path for the input JSON file
  -w WINDOW_SIZE, --window_size WINDOW_SIZE
                        Moving average window size in minutes
```

## Testing the Application

To validate the functionality of the application, a set of tests has been provided in the "tests" folder. To run the tests, use the following command from the root of the repository:

 ```pytest moving_average_tests.py```

This will execute the test suite and verify that the application performs as intended.

And that's it! Thank you, and happy coding!

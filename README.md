# AirBnB clone - The console

## Description
The is project focuses on the console part of the airbnb clone.

# Using the Console
The AirBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.
``` bash 
    $ echo "help" | ./console.py
    (hbnb) 
    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update
    (hbnb) 
    $ 
```
Alternatively, to use the AirBnB console in interactive mode, run the file console.py by itself:
``` bash
    $ ./console.py
``` 
While running in interactive mode, the console displays a prompt for input:
``` bash
    $ ./console.py
    (hbnb) 
```
To quit the console, enter the command quit, or input an EOF signal (ctrl-D).
``` bash
    $ ./console.py
    (hbnb) quit
    $
```
``` bash
    $ ./console.py
    (hbnb) EOF
    $
```

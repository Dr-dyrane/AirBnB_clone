# AirBnB Clone

<p align="center">
  <img src="./assets/hbnb.png" alt="HolbertonBnB logo">
</p>

## Table of Contents

- [Description](#description)
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Description

AirBnB Clone is a web application developed as part of ALX group project by Ukpono Umoren and Alexander Udeogaranya. It aims to replicate the core functionalities of the popular online lodging marketplace, Airbnb.

## Project Overview

The AirBnB Clone project implements a custom command-line interface for data management, as well as the base classes for storing the data. It follows an Object-Oriented Programming (OOP) approach and includes features such as serialization, deserialization, and a file storage engine.

## Getting Started

To get started with the AirBnB Clone project, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Dr-dyrane/AirBnB_clone.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Start the console:

   ```
   python console.py
   ```

## Usage 💻

The AirBnB Clone console provides a command-line interface to manage the objects of the AirBnB project. You can create new objects, retrieve existing objects, perform operations on objects, update attributes, and destroy objects.

Refer to the console commands and syntax documentation for detailed usage instructions.

| Command                                       | Example                                                                                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Run the console                               | `./console.py`                                                                                                                            |
| Quit the console                              | `(hbnb) quit`                                                                                                                             |
| Display the help for a command                | `(hbnb) help <command>`                                                                                                                   |
| Create an object (prints its id)              | `(hbnb) create <class>`                                                                                                                   |
| Show an object                                | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)`                                                                                 |
| Destroy an object                             | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)`                                                                           |
| Show all objects, or all instances of a class | `(hbnb) all` or `(hbnb) all <class>`                                                                                                      |
| Update an attribute of an object              | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")` |

### Interactive mode (example)

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-interactive mode (example)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Testing

To run the unit tests for the project, use the following command:

```
python3 -m unittest discover tests/
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Contributing

Contributions to the AirBnB Clone project are welcome. If you find any bugs, have suggestions for improvements, or want to add new features, feel free to submit a pull request.

Please ensure that your contributions adhere to the project's coding standards and follow the established conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors

- [Ukpono Umoren](https://github.com/Ukeremi)
- [Alexander Udeogaranya](https://github.com/Dr-dyrane)

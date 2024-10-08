# Rock Paper Scissors Game

<img src="https://img.shields.io/badge/Python-3.x-blue" alt="Python"> <img src="https://img.shields.io/badge/Typer-0.12.3-green" alt="Typer"> <img src="https://img.shields.io/badge/Rich-13.7.1-purple" alt="Rich"> <img src="https://img.shields.io/badge/SQLAlchemy-2.0.31-red" alt="SQLAlchemy"> <img src="https://img.shields.io/badge/Socket-yellow" alt="Socket">

## Description
A simple Rock Paper Scissors game implemented in Python.

## Features
- Play against the computer
- Play against many player (No limit !)
- Randomized computer moves
- Score tracking

## Installation

### Prerequisites
- Python 3.x
- pip

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/serene1212/rock-paper-scissors.git
    cd rock_paper_scissors
    ```
2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
## Contribute

3 - Make a copy of `sample.env` and change the variables
```bash
cp sample.env .env
```

4 - Run the following command to apply migrations to the database
```bash
alembic upgrade head
```

## Usage
Run the game using the following command:
```sh
./run.sh
```
## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for more details.



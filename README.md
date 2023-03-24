# Next Watch
 Task submission for HyperionDev on semantic similarity 



## Installation

### Download the Repository
Click on the "Code" button on this repository and select "Download ZIP". Alternatively, you can clone the repository using Git with the following command:

git clone https://github.com/Olliebrou/Next-watch.git
Extract the ZIP file to your desired location.

Open a terminal window and navigate to the directory where you extracted the repository.

### This project uses Python.
If you do not have Python, you can download it here: https://www.python.org/downloads/

Use the following commands to install pip, a virtual environment and Django on a windows machine:
python -m pip install pip
pip install virtualenv
pip install virtualenvwrapper-win
mkvirtualenv <choose a name for your virtual environment>

This should automatically activate the virtual environment.

Open a terminal window and navigate to the directory where you saved the repo.


## Dependencies
In the project directory, you will find a requirements.txt file which lists all the required dependencies.

To download the dependencies, run the following command in the terminal while your virtual environment is activated:

pip install -r requirements.txt


## Running the program
Use the command line and run: python next_watch.py 

## Docker Setup
Download and install Docker from the official website: https://www.docker.com/get-started

Navigate to the root project directory in your terminal.

Build the Docker container using the included Dockerfile with the following command:

docker build -t next_watch .

Run the container using the following command:

docker run next_watch

The output of the program should appear in the command terminal

## Usage
The program is intended as a task submission. It will output very simple command line text. To view the code, either view directly on GitHub or open the .py files in an IDE of your choice.



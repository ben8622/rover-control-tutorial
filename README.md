# rover-control-tutorial
This repo is to demonstrate on a basic level how UTA's mars rover is controlled.

## Setup
It is highly recommended to use [virtual environments](https://docs.python.org/3/tutorial/venv.html) within python to seperate each of your projects dependancies.  

1. Start your virutal environment, if you are using one. How to do this is dependant on your OS, for windows run: `.\.venv\Scripts\activate` where `.venv` is the directory that you created the virtual environment in.
2. Install the required libraries using the `requirements.txt` file *(there is only one in this tutorial that is not included in python's standard library)* `pip install -r requirements.txt`

## Domain Model Diagram
This is the domain model diagram that represents the system we are building. It is very similar to how the Rover's systems function.  
![Rover Controls Domain Model Diagram](./imgs/rover-controls-DomainModelDiagram.png)  

## Running 
To run the program(s) you need 

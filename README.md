# A Open Library python Consumer
Uses urllib3 to consume, and MongoDB to store the data, this python repository has the objective to rank the top 10 most recurrent words in titles.

## Getting Started
**First you'll need to install:**

MongoDB - MongoDB is a general purpose, document-based, distributed database  
`$ sudo apt update`  
`$ sudo apt install -y mongodb`  

[Python3](https://www.python.org/downloads/)  
`$ sudo apt-get install python3`

Pip3  
`$ sudo apt install python3-pip` 

PyMongo - A Python distribution containing tools to work with MongoDB, and is the recommended way to work with MongoDB from Python.  
`$ pip3 install pymongo`

Loguru - Loguru is a library which aims to bring enjoyable logging in Python.   
`$ pip3 install loguru`

Urllib3 - It's a powerful HTTP client for Python.  
`$ pip3 install urllib3`

## Getting started

It is recommended to use a virtual environment to install the Python libraries, you can find the documentation [here](https://docs.python.org/3/library/venv.html)
1- using pip3 and the requirements file, install the needed libraries.  
`pip3 install -r requirements.txt`

2- Runs the main.py file with Python3.

3- Running the main.py with no parameters will use the default configuration(query = 'lord', pages_number = 64, page_limit = 1000).  

4- Using the '-m' flag open the possibilities to custom the configurations.  
`python3 main.py -m <query> <pages_number> <page_limit>`

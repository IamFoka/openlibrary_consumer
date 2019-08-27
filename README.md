# A Open Library python Consumer
Uses urllib3 to consume, and MongoDB to store the data, this python repository has the objective to rank the top 10 most recurrent words in titles.

## Getting Started
**First you'll need to install:**

[MongoDB](https://docs.mongodb.com/manual/tutorial/getting-started/) - MongoDB is a general purpose, document-based, distributed database  
`$ sudo apt update`  
`$ sudo apt install -y mongodb`  

[Python3](https://www.python.org/downloads/)  
`$ sudo apt-get install python3`

Pip3  
`$ sudo apt install python3-pip` 

[PyMongo](https://api.mongodb.com/python/3.6.0/tutorial.html) - A Python distribution containing tools to work with MongoDB, and is the recommended way to work with MongoDB from Python.  
`$ pip3 install pymongo`

[Loguru](https://github.com/Delgan/loguru) - Loguru is a library which aims to bring enjoyable logging in Python.   
`$ pip3 install loguru`

[Urllib3](https://urllib3.readthedocs.io/en/latest/) - It's a powerful HTTP client for Python.  
`$ pip3 install urllib3`

## How to run

It is recommended to use a virtual environment to install the Python libraries, you can find the documentation [here](https://docs.python.org/3/library/venv.html)  
1- using pip3 and the requirements file, install the needed libraries.  
`pip3 install -r requirements.txt`

2- Runs the main.py file with Python3.

3- Running the main.py with no parameters will use the default configuration(query = 'lord', pages_number = 64, page_limit = 1000).  

4- Using the '-m' flag open the possibilities to custom the configurations.  
`python3 main.py -m <query> <pages_number> <page_limit>`

## Results
![image](https://user-images.githubusercontent.com/40413290/63745747-58ec7400-c879-11e9-97f3-56a1e81155e6.png)

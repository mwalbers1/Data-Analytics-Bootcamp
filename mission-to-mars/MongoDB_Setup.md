# MongoDB Setup

## MongoDB
MongoDB (also known as Mongo) is a document database that thrives on chaos. Well, maybe it's not that extreme, but it is far more flexible when storing data than a structured database such as SQL. It's able to handle smaller, more personal projects and larger-scale projects that a company might require. Mongo is a better choice than SQL because the data scraped from the web isn't going to be uniform. For example, how would we break down an image into rows and columns? We can't. But Mongo will store and access it as a document instead.

To install PyMongo, first, open an Anaconda terminal window (make sure your virtual environment is active). Then execute the "pip install pymongo" command. PyMongo is the tool that allows developers to use Python with Mongo.

## Windows Installation
To install Mongo on your Windows computer, follow the instructions: Install MongoDB Community Edition on Windows.  Be sure to follow all of the steps listed for installing the MongoDB Community Edition.

Add a data directory to the root folder:

```bash
cd c:\
mkdir data\db
```

The `data\db`  is the default location for Mongo's databases. 

Then add MongoDB's path to the **PATH** environment variables for your computer so that you can run and launch MongoDB quickly from the command line.

First, locate the directory where you installed MongoDB. This is likely `C:\Program Files\MongoDB\Server\bin`. Copy this directory to your clipboard with **CTRL + C**. Then add it to the **PATH** environment variable.

To test if this worked, close your current Anaconda Prompt window, reopen it and run this command: `mongod`. If Mongo continues to run in the terminal, it's been successfully installed.

## Additional Libraries
Both `html5lib` and `lxml` packages are used to parse HTML in Python, which will be necessary for traversing different web pages to find and collect information.

First, make sure your coding environment is active. Then, type the following commands in your terminal to install them:

```bash
pip install html5lib
pip install lxml
```

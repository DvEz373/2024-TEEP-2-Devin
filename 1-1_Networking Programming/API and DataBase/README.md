# Network Programming - API and DB
- [Network Programming - API and DB](#network-programming---api-and-db)
  - [1. Application Programming Interface (API)](#1-application-programming-interface-api)
    - [1.1. API in Telecommunication Systems](#11-api-in-telecommunication-systems)
    - [1.2. API Monetize Network](#12-api-monetize-network)
    - [1.3. Elements in an URL APIs](#13-elements-in-an-url-apis)
  - [2. DataBase (DB)](#2-database-db)
    - [2.1. Types of DataBase](#21-types-of-database)
    - [2.2. API and DB in a System](#22-api-and-db-in-a-system)
  - [3. Network Programming](#3-network-programming)
  - [4. Building API Server and Connecting to Database](#4-building-api-server-and-connecting-to-database)

## 1. Application Programming Interface (API)
![image](https://hackmd.io/_uploads/ryjXDSfuT.png)

<div class="text-justify">
APIs are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols. For example, the weather bureau’s software system contains daily weather data. The weather app on your phone “talks” to this system via APIs and shows you daily weather updates on your phone.
</div>
<br>
<div class="text-justify">
In the context of APIs, the word Application refers to any software with a distinct function. Interface can be thought of as a contract of service between two applications. This contract defines how the two communicate with each other using requests and responses. Their API documentation contains information on how developers are to structure those requests and responses.
</div>
<br>
<div class="text-justify">
API architecture is usually explained in terms of client and server. The application sending the request is called the client, and the application sending the response is called the server. So in the weather example, the bureau’s weather database is the server, and the mobile app is the client. There are four different ways that APIs can work depending on when and why they were created.
    
* SOAP APIs 
These APIs use Simple Object Access Protocol. Client and server exchange messages using XML. This is a less flexible API that was more popular in the past.
* RPC APIs
These APIs are called Remote Procedure Calls. The client completes a function (or procedure) on the server, and the server sends the output back to the client.
* Websocket APIs
Websocket API is another modern web API development that uses JSON objects to pass data. A WebSocket API supports two-way communication between client apps and the server. The server can send callback messages to connected clients, making it more efficient than REST API.
* REST APIs
These are the most popular and flexible APIs found on the web today. The client sends requests to the server as data. The server uses this client input to start internal functions and returns output data back to the client. REST stands for Representational State Transfer. REST defines a set of functions like GET, PUT, DELETE, etc. that clients can use to access server data. Clients and servers exchange data using HTTP.
The main feature of REST API is statelessness. Statelessness means that servers do not save client data between requests. Client requests to the server are similar to URLs you type in your browser to visit a website. The response from the server is plain data, without the typical graphical rendering of a web page.
</div>

### 1.1. API in Telecommunication Systems
<div class="text-justify">
APIs (Application Programming Interfaces) play a vital role in telecommunications by enabling:
    
* **Integration and Innovation**: Telecom APIs allow providers to combine services and systems from different sources, fostering partnerships that lead to innovative offerings and accelerated development of high-quality services.
* **Data Sharing and Access**: They facilitate the exchange of data between telecom companies and enterprises, exposing services like voice, messaging, location, and payment to external applications.
* **Enhanced Customer Experiences**: APIs enable seamless integration of telecom features into various applications, offering personalized and convenient services
* **New Services and Capabilities**: They support the development of wide-area IoT solutions, collection of data from IoT devices, and creation of services that function independently of devices.
* **Strategic Partnerships**: Telecom APIs open up telecom resources to enterprises, allowing them to leverage the power of telecom networks.
    
APIs (Application Programming Interfaces) play a crucial role in unlocking the potential of 5G networks by:
1. **Exposing Network Capabilities**: 5G APIs enable developers to access and utilize the advanced features and functionalities of 5G networks, such as high bandwidth, low latency, and massive device connectivity. The creation of innovative applications and services leverage the unique capabilities of 5G, such as immersive experiences, real-time automation, and enhanced connectivity.
2. **Enabling Network Programmability**: 5G networks are designed to be more programmable and flexible than previous generations. APIs allow operators to dynamically adjust network resources and configurations to meet specific needs and optimize performance.
3. **Fostering Collaboration and Ecosystem Development**: Standardized 5G APIs promote collaboration between network operators, application developers, and other stakeholders, leading to a thriving ecosystem of 5G-enabled solutions.
4. **Enhancing Network Awareness and Control**: Applications can gain real-time awareness of network conditions and make informed decisions using 5G APIs.
</div>

### 1.2. API Monetize Network
<div class="text-justify">
Network APIs expose network features like network slicing, edge computing, and ultra-low latency to developers, enabling innovative services. Network operators can charge for API usage, create partnerships, or offer value-added services to generate revenue in addition to make more revenue streams. APIs foster collaboration with third-party developers, accelerating innovation and service creation.
    
Some implementation of Network APIs especially in 5G network system:
* **Network Slicing as a Service**: Providing tailored network slices for specific industry needs.
* **Enhanced Mobile Broadband**: Offering premium QoS for high-bandwidth applications.
* **Massive IoT Connectivity**: Enabling large-scale IoT deployments with efficient API-based management.
</div>

### 1.3. Elements in an URL APIs
Basically, in an Uniform Resource Locator (URL) or a link of an APIs consists of several common elements. APIs use URLs to specify the location of a resource. The URL is composed of several parts. Those elements are such as:
- **Protocol**: The protocol specifies the communication protocol used by the client and server. Common protocols include HTTP, HTTPS, and FTP.
- **Domain name**: The domain name identifies the server that hosts the resource. For example, in the URL `https://www.example.com/index.html`, the domain name is `www.example.com`.
- **Port number**: The port number is used to identify the specific process on the server that is handling the request. If no port number is specified, the default port for the protocol is used (e.g., port 80 for HTTP).
- **Path**: The path specifies the location of the resource on the server. For example, in the URL `https://www.example.com/index.html`, the path is `/index.html`.
- **Query parameters**: Query parameters are used to pass additional information to the server. They are appended to the end of the URL and separated by `&` characters. For example, in the URL `https://www.example.com/search?q=example&limit=10`, the query parameters are `q=example` and `limit=10`.
- **Fragment identifier**: The fragment identifier specifies a specific section of the resource. It is preceded by a `#` character. For example, in the URL `https://www.example.com/index.html#section1`, the fragment identifier is `section1`.



## 2. DataBase (DB)
![image](https://hackmd.io/_uploads/ByPQY2mda.png)
<div class="text-justify">
    
A **database** is an organized collection of structured information or data that is typically stored electronically in a computer system. It is usually controlled by a **database management system (DBMS)**, which is a software that interacts with end-users, applications, and the database itself to capture and analyze the data. Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a **database system**. The data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and data querying efficient. The data can then be easily accessed, managed, modified, updated, controlled, and organized. Most databases use **Structured Query Language (SQL)** for writing and querying data. There are many different types of databases, and the best database for a specific organization depends on how the organization intends to use the data.
    
</div>

### 2.1. Types of DataBase
<div class="text-justify">

There are many different types of databases, each with its own strengths and weaknesses. Here are some of the most common types of databases:
1. **Relational database**: This is the most widely used type of database. It stores data in tables with rows and columns, and uses SQL for querying and managing data. 
2. **NoSQL database**: This type of database is designed to handle large volumes of unstructured data. It does not use tables, and instead stores data in a variety of formats such as key-value pairs, documents, and graphs.
3. **Object-oriented database**: This type of database stores data in objects, which are instances of classes. It is designed to handle complex data structures and relationships.
4. **Hierarchical database**: This type of database organizes data in a tree-like structure, with each record having a parent-child relationship with other records ¹.
5. **Network database**: This type of database is similar to a hierarchical database, but allows each record to have multiple parent records.
6. **Cloud database**: This type of database is hosted on a cloud platform, and provides scalability, flexibility, and cost-effectiveness.
7. **Centralized database**: This type of database stores all data in a single location, making it easy to manage and control.
8. **Distributed database**: This type of database stores data across multiple locations, making it more fault-tolerant and scalable.
9. **Operational database**: This type of database is designed to handle real-time processing of data, and is used for transactional systems such as banking and e-commerce. 
10. **Analytical database**: This type of database is designed to handle complex queries and data analysis, and is used for business intelligence and data warehousing.
11. **Graph database**: This type of database is designed to handle data with complex relationships, and is used for social networks, recommendation engines, and fraud detection.

</div>

### 2.2. API and DB in a System
![image](https://hackmd.io/_uploads/rJuBYnm_T.png)
<div class="text-justify">
APIs and databases are two essential components of modern software systems. APIs, or Application Programming Interfaces, are used to enable communication between different software components, while databases are used to store and manage data. APIs are often used as intermediaries to facilitate the retrieval and manipulation of data stored in databases by various applications. When a client application sends a request to an API, the API server processes the request and retrieves the necessary data from the database. The API then sends the data back to the client application in a format that can be easily consumed by the application. In this way, APIs and databases work together to provide a seamless experience for the end user.
For example, consider a mobile application that allows users to search for products on an e-commerce website. When the user enters a search query, the mobile application sends a request to the API server, which retrieves the relevant data from the database. The API then sends the data back to the mobile application, which displays the results to the user.
    
In the context of APIs and databases, some functions are used to interact with the datas in the database like CRUD and HTTP Functions. **CRUD** stands for **Create**, **Read**, **Update**, and **Delete**. These are the four major functions for interacting with database applications. CRUD functions often play a role in web-based REST APIs, where they map to the HTTP methods **GET**, **POST**, **DELETE**, **PUT**, and **PATCH**. 
Here is a brief description of each CRUD function and its corresponding HTTP method:

- **Create**: This function is used to create a new resource in the database. In HTTP, the **POST** method is used to create a new resource. For example, when a user submits a form on a website, the data from that form needs to be stored in a database. This involves creating a new record in the database.
- **Read**: This function is used to retrieve an existing resource from the database. In HTTP, the **GET** method is used to retrieve data from a resource. For example, when a user wants to view their account information on a website, the application needs to be able to retrieve that information from the database.
- **Update**: This function is used to modify an existing resource in the database. In HTTP, the **PUT** method is used to update an existing resource, while the **PATCH** method is used to update a part of an existing resource. For example, when a user wants to update their account information on a website, the application needs to be able to modify the corresponding record in the database.
- **Delete**: This function is used to remove an existing resource from the database. In HTTP, the **DELETE** method is used to delete a resource. For example, when a user wants to delete their account information on a website, the application needs to be able to remove the corresponding record from the database.
</div>

## 3. Network Programming
![image](https://hackmd.io/_uploads/HJtsF37Oa.png)
<div class="text-justify">
    
In this context, network programming focuses on writing **code or program** so that the we can **communicate** with **other computers or external devices** via **network** such as internet.
Network programming is used to enable communication between different software components, such as client applications, APIs, and databases. APIs are used to enable communication between different software components, while databases are used to store and manage data. APIs are often used as intermediaries to facilitate the retrieval and manipulation of data stored in databases by various applications. When a client application sends a request to an API, the API server processes the request and retrieves the necessary data from the database. The API then sends the data back to the client application in a format that can be easily consumed by the application. In this way, APIs and databases work together to provide a seamless experience for the end user. 
    
**TCP/IP** and **UDP/IP** are two of the most commonly used protocols for network communication. TCP/IP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data between applications. UDP/IP, on the other hand, is a connectionless protocol that provides unreliable, unordered, and unacknowledged delivery of data between applications. There are also other protocols like **HTTP, HTTPS and MQTT**.
    
**TLI** and **socket API** are two programming interfaces that can be used for network programming. TLI, or Transport Layer Interface, is a programming interface that provides a high-level interface to network protocols such as TCP/IP and UDP/IP. Socket API, on the other hand, is a low-level interface that provides access to the underlying network protocols.
    
Network programming is **essential** for building modern software systems that rely on APIs and databases. It enables different software components to communicate with each other over a network, and facilitates the retrieval and manipulation of data stored in databases by various applications. 
</div>

## 4. Building API Server and Connecting to Database
1. The first thing that we have to do is to create the database itself. I am using MySQL because it is free and open source available. There are other database framework that can also be used such as Firebase and MongoDB. For this practice example, I am building this API from scratch in Python. For the database I am using XAMPP to use MySQL.
2. The second thing that we have to do is to activate the local host from XAMPP to access our MySQL database. In this practice example I am going to make a database for storing data of products. In the XAMPP Control Panel we have to activate Apache and MySQL
![image](https://hackmd.io/_uploads/BkTsKNB_T.png)
3. Now, we have to create a database. I named the database "product" in phpMyAdmin. I accessed it from the Admin button in the control panel.
4. After I create an empty database, I build the API Server with Flask in Python. First I import some necessary libraries:
```python
from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow
```
5. Then we need to create instances of flask and mysql db like this:
```python
app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow()
mysql = MySQL(app)
```
6. After that we can start build our database. Here I use a table model that stores data consists of id, name, price and category. I create a class for handling the model as such:
```python
class Product(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(15), nullable=False)
    price= db.Column(db.Float, nullable=False)
    category= db.Column(db.String(15), nullable=False)


    def __init__(self, name, price, category) :
        self.name=name
        self.price=price
        self.category=category
```
![image](https://hackmd.io/_uploads/SJ-LzBrup.png)
This is the table that I have created from the model in the Class definition above in phpMyAdmin.
7. After that, we will have to initialize the database and API server by using this code:
```python
# MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/product'

# SQLITE
db.init_app(app)
with app.app_context():
    db.create_all()
```
8. The next step is to create some features for example in this practice I am adding the features to add product data, delete product data, get product data, and edit product data. These features are seperated into some functions below:
* Add Product Function
```python
@app.route('/product/add', methods=['POST'])
def add_product():
    _json = request.json
    name = _json['name']
    price = _json['price']
    category = _json['category']
    new_product = Product(name=name, price=price, category=category)
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "the product has been added "})
```
In this code, first we need to define the root that will be the address to access the feature functions. In this example it is '/product/add'. Then the data got passed as a JSON data type.
* Get Product Function
```python
@app.route('/product', methods=['GET'])
def get_product():
    products = []
    data = Product.query.all()
    products = products_schema.dump(data)
    return jsonify(products)


@app.route('/product/<id>', methods=['GET'])
def product_byid(id):
    product = Product.query.get(id)
    data = product_schema.dump(product)
    return jsonify(data)
```
For the get product feature, we need to make product schema for best practice because the method in this feature is 'GET' and it is different from other features. I add another class for the product schema:
```python
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name', 'price', 'category')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
```
This class is defined before the initialization of MySQL and SQLite for the Database and Flask for the API Server.
* Delete Product Function 
```python
@app.route('/product/delete/<id>', methods=['POST'])
def delete_product(id):
    product = Product.query.get(id)
    if product is None:
        return jsonify(f"Error: the product doesn't exist")
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "the product has been deleted"})
```
* Edit Product Function
```python
@app.route('/product/edit/<id>', methods=['POST'])
def edit_product(id):
    product = Product.query.get(id)
    if product is None:
        return jsonify ({"error": "the prodcut doesn't exist"})
    _json = request.json
    product.name = _json['name']
    product.price =_json['price']
    product.category= _json['category']
    db.session.commit()
    return jsonify({"message": "the product has been edited"})
```
9. Lastly, the main function is:
```python
if __name__ == "__main__":
    app.run(debug=True)
```
10. To test the API Server and the Database, I will be using **Postman** to POST data into my database via API Server that I just make and also test to GET data. In this example, I am going to try to add data to the database by using POST method in the API Server.

![image](https://hackmd.io/_uploads/rJ6bjH8u6.png)

This is the example. I add a product data in JSON. When we see it in the database, it will be added.

![image](https://hackmd.io/_uploads/ryq_iSI_p.png)

We can also see the JSON data from the API Server like this:

![image](https://hackmd.io/_uploads/SJansH8_a.png)

11. 
# Python Hiring Task - APIs using FastAPI

This project is focused on building REST APIs using FastAPI and MongoDB. API built in this project allows users to:

- Create, Read, Update, and Delete products
- Place orders (nested objects)
- Fetch all orders
- Search an order by its Order ID

---

## Setup on Local System

Clone the repository:

	git clone https://github.com/KartikDholakia/cosmo_api

Move into that directory:

	cd cosmo_api

Install the required libraries:

	pip install requirements.txt

Run the server:

	uvicorn main:app --reload

---

## Configure the Database

MongoDB Database was used in this project. In order to connect with the database, create a cluster in MongoDB Atlas and then create a database.

Then create a .env file:

	MONGODB_CONNECTION_URI=<place-your-connection-string>
	DB_NAME=<database-name>

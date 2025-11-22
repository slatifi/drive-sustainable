# API Exercise

In this exercise, we will continue with our `Basket` service by adding a RESTful API using Flask. This will allow clients to interact with the basket via HTTP requests.
We will implement endpoints to **add** items, **remove** items, **view the contents** of the basket and get the **total price**.

### Instructions

In the `exercise` directory, locate the `api.py` file - it currently contains the examples from the slides. Your task is to implement the following endpoints:

1. **Add Item**:
   - **Endpoint**: `POST /basket`
   - **Request Body**: JSON object with `name` (string).
   - **Functionality**: Increments the quantity of the specified item in the basket by 1. If the item does not exist, it should be added with a quantity of 1.
   - **Response**: Return a success message.
2. **Remove Item**:
   - **Endpoint**: `DELETE /basket`
   - **Request Body**: JSON object with `name` (string).
   - **Functionality**: Decrements the quantity of the specified item in the basket by 1. If the item's quantity reaches 0, it should be removed from the basket.
   - **Response**: Return a success message.
3. **View Basket**:
   - **Endpoint**: `GET /basket`
   - **Functionality**: Returns the current contents of the basket as a JSON object which a root array called `items`. Each item in the array should be an object with `name` and `quantity`.
4. **Get Total Price**:
   - **Endpoint**: `GET /basket/total`
   - **Functionality**: Returns the total price of all items in the basket as a JSON object with a single key `price`.

---

### Client

In order to test your API, there is a simple web client in `exercise/client.html`.

Open this file in your web browser and use the interface to interact with your API. You can add items, remove items, view the basket contents, and see the total price.

It will only work if your API server is implemented to the specifications above.

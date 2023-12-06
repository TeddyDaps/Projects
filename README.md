# "SWE4001 - Introduction to Software Development"
"A café wants to track the orders it receives for home delivery over the phone.

The café has a number of employees who will be using the system:

Clerks: They enter orders and check for pending orders.
Delivery: They deliver the orders and update the system upon order completion.
Manager: They view summary reports and statistics.
Each employee has an account for system use (username/password), and the system must recognize their respective roles.

For each order, each clerk can enter into the system:

Customer's name
Customer's address
Description (contents of the order)
Date (format: DDMMYY)
Total order amount
The system assigns an automatically incremented ID code for each new order.

Each clerk can input orders in bulk from a properly formatted file (txt or csv).

Each clerk can also view orders that have not been delivered.

After delivering an order, the delivery employee updates it as completed.

Managers can select functions such as:

Number of orders from a specific customer
Number of orders on a given day
Total number of delivered orders
Total amount of orders from a specific customer
Total amount of orders on a given day

Managers can also request data export into a file (csv format) for the following:
Customer names
Number of orders entered by each clerk
All orders that have been registered
Total order amount per day.
**MySQL Query Generator**

This Python script is an interactive MySQL query generator and executor. It helps users generate common SQL queries (SELECT, UPDATE, DELETE, and INSERT) through a user-friendly command-line interface. Users are prompted for query details step-by-step, allowing even those with minimal SQL experience to create valid queries.

### Features:
- **Interactive Query Generation**: Generate SELECT, UPDATE, DELETE, and INSERT queries by providing input through a series of prompts.
- **JOIN, WHERE, ORDER BY, and LIMIT Clauses**: Supports the creation of JOIN, WHERE, ORDER BY, and LIMIT clauses for more flexible and complex query generation.
- **Execute Queries**: Optionally execute the generated query on a MySQL database.
- **Export Results**: For SELECT queries, view the results in a DataFrame and save them to an Excel file.
- **Beautified Output**: Displays clear, formatted text outputs to enhance the user experience.

### How to Use:
1. Run the script and choose the type of query you want to generate.
2. Follow the prompts to specify tables, columns, conditions, and other query details.
3. Optionally execute the query directly on your MySQL server.
4. For SELECT queries, save the output to an Excel file if needed.

### Requirements:
- Python 3
- `mysql-connector-python` for connecting to MySQL.
- `pandas` for displaying and saving query results.

### Installation:
```sh
pip install mysql-connector-python pandas
```

### Example Usage:
```sh
python mysql_query_generator.py
```
Generate a SELECT query for the `employees` table, add filtering conditions, execute it on the database, and optionally save the results to an Excel file.

### Note:
Ensure that you have valid credentials for your MySQL server, and the appropriate permissions to execute the desired queries.

This tool is designed to assist users in quickly building and running SQL queries, making it easier to interact with MySQL databases without manually writing complex SQL code.


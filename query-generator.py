import mysql.connector
import pandas as pd

def main():
    print("\nWelcome to the MySQL Query Generator!\n")
    while True:
        print("\n1. SELECT Query\n2. UPDATE Query\n3. DELETE Query\n4. INSERT Query\n5. Exit")
        query_type = input("Select the type of query you want to generate (1-5): ").strip()
        if query_type == "1":
            generate_select_query()
        elif query_type == "2":
            generate_update_query()
        elif query_type == "3":
            generate_delete_query()
        elif query_type == "4":
            generate_insert_query()
        elif query_type == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option selected. Please try again.")


def generate_select_query():
    table = input("Enter the table name (e.g., employees, products): ")
    columns = input("Enter columns to select (comma-separated, or * for all columns, e.g., name, age, department): ")
    join_clause = get_join_clause()
    where_clause = get_where_clause()
    order_by_clause = get_order_by_clause()
    limit_clause = get_limit_clause()
    
    query = f"SELECT {columns} FROM {table}"
    if join_clause:
        query += f" {join_clause}"
    if where_clause:
        query += f" WHERE {where_clause}"
    if order_by_clause:
        query += f" ORDER BY {order_by_clause}"
    if limit_clause:
        query += f" LIMIT {limit_clause}"
    
    print("\nGenerated SELECT Query:")
    print(query)
    execute_query(query, is_select=True)


def generate_update_query():
    table = input("Enter the table name (e.g., employees, products): ")
    set_clause = input("Enter the columns and values to update (e.g., column1='value1', column2='value2'): ")
    where_clause = get_where_clause()
    
    query = f"UPDATE {table} SET {set_clause}"
    if where_clause:
        query += f" WHERE {where_clause}"
    
    print("\nGenerated UPDATE Query:")
    print(query)
    execute_query(query)


def generate_delete_query():
    table = input("Enter the table name (e.g., employees, products): ")
    where_clause = get_where_clause()
    
    query = f"DELETE FROM {table}"
    if where_clause:
        query += f" WHERE {where_clause}"
    else:
        print("Warning: You are about to delete all rows in the table!")
        confirm = input("Are you sure you want to continue? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Delete query aborted.")
            return
    
    print("\nGenerated DELETE Query:")
    print(query)
    execute_query(query)


def generate_insert_query():
    table = input("Enter the table name (e.g., employees, products): ")
    columns = input("Enter columns to insert into (comma-separated, e.g., name, age, department): ")
    values = input("Enter values to insert (comma-separated, in the same order as columns, e.g., 'John', 30, 'Sales'): ")
    
    query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
    
    print("\nGenerated INSERT Query:")
    print(query)
    execute_query(query)


def get_where_clause():
    where_clause = ""
    add_more = True
    conditions = []
    while add_more:
        column = input("Enter column for WHERE condition (e.g., age, department): ")
        operator = input("Enter operator (=, !=, <, <=, >, >=, LIKE, IN, BETWEEN, IS NULL, IS NOT NULL): ")
        value = input("Enter value (use single quotes for strings, e.g., 'Sales', 30): ")
        conditions.append(f"{column} {operator} {value}")
        
        add_more_input = input("Do you want to add another condition? (yes/no): ").strip().lower()
        if add_more_input != 'yes':
            add_more = False
    
    if conditions:
        if len(conditions) > 1:
            logical_operator = input("Enter logical operator to combine conditions (AND/OR): ").strip().upper()
            where_clause = f" {logical_operator} ".join(conditions)
        else:
            where_clause = conditions[0]
    
    return where_clause


def get_join_clause():
    join_clause = ""
    add_join = input("Do you want to add a JOIN clause? (yes/no): ").strip().lower()
    if add_join == 'yes':
        join_type = input("Enter join type (INNER/LEFT/RIGHT/FULL): ")
        join_table = input("Enter the table to join (e.g., departments, orders): ")
        join_condition = input("Enter the join condition (e.g., table1.column = table2.column): ")
        join_clause = f"{join_type} JOIN {join_table} ON {join_condition}"
    
    return join_clause


def get_order_by_clause():
    order_by_clause = ""
    add_order_by = input("Do you want to add an ORDER BY clause? (yes/no): ").strip().lower()
    if add_order_by == 'yes':
        order_by_columns = input("Enter columns to order by (comma-separated, e.g., age, name): ")
        order_direction = input("Enter order direction (ASC for ascending, DESC for descending): ").strip().upper()
        order_by_clause = f"{order_by_columns} {order_direction}"
    
    return order_by_clause


def get_limit_clause():
    limit_clause = ""
    add_limit = input("Do you want to add a LIMIT clause? (yes/no): ").strip().lower()
    if add_limit == 'yes':
        limit_value = input("Enter the number of rows to limit the result to (e.g., 10, 100): ")
        limit_clause = f"{limit_value}"
    
    return limit_clause


def execute_query(query, is_select=False):
    execute = input("Do you want to execute this query on the MySQL database? (yes/no): ").strip().lower()
    if execute == 'yes':
        try:
            host = input("Enter MySQL host (e.g., localhost): ")
            user = input("Enter MySQL user: ")
            password = input("Enter MySQL password: ")
            database = input("Enter MySQL database name: ")
            port = int(input("Enter MySQL server port (default is 3306): "))

            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            cursor = connection.cursor()
            cursor.execute(query)
            if is_select:
                results = cursor.fetchall()
                columns = [i[0] for i in cursor.description]
                df = pd.DataFrame(results, columns=columns)
                print(df)
                save_to_excel = input("Do you want to save the results to an Excel file? (yes/no): ").strip().lower()
                if save_to_excel == 'yes':
                    df.to_excel("query_results.xlsx", index=False)
                    print("Results saved to query_results.xlsx")
            else:
                connection.commit()
                print("Query executed successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed.")
    else:
        print("Query execution skipped.")


if __name__ == "__main__":
    main()

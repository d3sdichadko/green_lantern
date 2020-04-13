from typing import List


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    sql_query = """
    INSERT INTO
    customers (customername, contactname, address, city, postalcode, country)
    VALUES
    (
      'Thomas', 'David', 'Some Address', 'London', '774', 'Singapore'
    );    
    """
    with con.cursor() as cur:
        cur.execute(sql_query)


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    sql_query = """
    SELECT * FROM Customers;
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    sql_query = """
    SELECT * FROM Customers WHERE country = 'Germany';
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    sql_query = """
    UPDATE Customers 
    SET customername = 'Johnny Depp'
    WHERE customerid = (SELECT MIN(customerid) FROM Customers); 
    """
    with con.cursor() as cur:
        cur.execute(sql_query)


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    sql_query = """
        DELETE FROM Customers         
        WHERE customerid = (SELECT MAX(customerid) FROM Customers); 
        """
    with con.cursor() as cur:
        cur.execute(sql_query)


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    sql_query = """
        SELECT Country FROM Suppliers;
        """
    cur.execute(sql_query)
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    sql_query = """
    SELECT Country FROM Suppliers ORDER BY Country DESC;
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    sql_query = """
    SELECT COUNT(CustomerID),City FROM Customers GROUP BY City ORDER BY City DESC;
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    sql_query = """
    SELECT COUNT(CustomerID),Country
    FROM Customers
    GROUP BY Country
    HAVING COUNT(CustomerID) > 10
    ORDER BY COUNT(CustomerID) DESC, country;
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    sql_query = """
    SELECT * FROM Customers
    ORDER BY CustomerID
    LIMIT 10;
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    sql_query = """
    SELECT * FROM Customers
    ORDER BY CustomerID
    OFFSET 11 ROWS;
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    sql_query = """
    SELECT supplierid,suppliername,contactname,city,country
    FROM Suppliers
    WHERE country IN ('USA', 'UK', 'Japan')
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    sql_query = """
    SELECT ProductName FROM Products
    INNER JOIN Suppliers
    ON Suppliers.SupplierID = Products.SupplierID
    WHERE Suppliers.Country = 'Sweden'
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    sql_query = """
    SET LOCAL lc_monetary = 'en_US.UTF-8';
    SELECT productid,productname,unit,price,country,city,suppliername FROM Products
    INNER JOIN Suppliers
    ON Suppliers.SupplierID = Products.SupplierID
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    sql_query = """
    SELECT customername,contactname,country,orderid FROM Customers
    INNER JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID
    """
    cur.execute(sql_query)
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    sql_query = """
    SELECT
       customername,
       cust.address,
       cust.country as customercountry,
       supp.country as suppliercountry,
       suppliername 
    FROM
       Customers as cust 
    FULL OUTER JOIN
       Suppliers as supp 
    USING(country)
    ORDER BY customercountry,suppliercountry
    """
    cur.execute(sql_query)
    return cur.fetchall()

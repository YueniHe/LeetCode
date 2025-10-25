import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    find_customers=customers[~customers['id'].isin(orders['customerId'])]
    find_customers=find_customers[['name']].rename(columns={'name':'Customers'})
    return find_customers
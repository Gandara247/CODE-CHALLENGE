# Constantes para as tabelas
CATEGORIES = "categories"
SUPPLIERS = "suppliers"
PRODUCTS = "products"
CUSTOMER_DEMOGRAPHICS = "customer_demographics"
CUSTOMER_CUSTOMER_DEMO = "customer_customer_demo"
CUSTOMERS = "customers"
REGION = "region"
TERRITORIES = "territories"
EMPLOYEES = "employees"
EMPLOYEE_TERRITORIES = "employee_territories"
US_STATES = "us_states"
SHIPPERS = "shippers"
ORDERS = "orders"
ORDER_DETAILS = "order_details"

# Constantes para as colunas
CATEGORY_ID = "category_id"
SUPPLIER_ID = "supplier_id"
PRODUCT_ID = "product_id"
CUSTOMER_TYPE_ID = "customer_type_id"
CUSTOMER_ID = "customer_id"
REGION_ID = "region_id"
TERRITORY_ID = "territory_id"
EMPLOYEE_ID = "employee_id"
REPORTS_TO = "reports_to"
STATE_ID = "state_id"
SHIPPER_ID = "shipper_id"
ORDER_ID = "order_id"

# Índices das tabelas
table_idx = {
    CATEGORIES: [CATEGORY_ID],
    SUPPLIERS: [SUPPLIER_ID],
    PRODUCTS: [PRODUCT_ID],
    CUSTOMER_DEMOGRAPHICS: [CUSTOMER_TYPE_ID],
    CUSTOMER_CUSTOMER_DEMO: [CUSTOMER_ID, CUSTOMER_TYPE_ID],
    CUSTOMERS: [CUSTOMER_ID],
    REGION: [REGION_ID],
    TERRITORIES: [TERRITORY_ID, REGION_ID],
    EMPLOYEES: [EMPLOYEE_ID, REPORTS_TO],
    EMPLOYEE_TERRITORIES: [EMPLOYEE_ID, TERRITORY_ID],
    US_STATES: [STATE_ID],
    SHIPPERS: [SHIPPER_ID],
    ORDERS: [ORDER_ID],
    ORDER_DETAILS: [ORDER_ID, PRODUCT_ID]
}

# Relações entre as tabelas
table_relationships = {
    PRODUCTS: [
        [CATEGORIES, CATEGORY_ID],
        [SUPPLIERS, SUPPLIER_ID]
    ],
    CUSTOMER_CUSTOMER_DEMO: [
        [CUSTOMER_DEMOGRAPHICS, CUSTOMER_TYPE_ID]
    ],
    CUSTOMERS: [
        [CUSTOMER_CUSTOMER_DEMO, CUSTOMER_ID]
    ],
    TERRITORIES: [
        [REGION, REGION_ID]
    ],
    EMPLOYEES: [
        [EMPLOYEES, REPORTS_TO]
    ],
    EMPLOYEE_TERRITORIES: [
        [TERRITORIES, TERRITORY_ID],
        [EMPLOYEES, EMPLOYEE_ID]
    ],
    ORDERS: [
        [CUSTOMERS, CUSTOMER_ID],
        [EMPLOYEES, EMPLOYEE_ID],
        [SHIPPERS, SHIPPER_ID]
    ],
    ORDER_DETAILS: [
        [ORDERS, ORDER_ID],
        [PRODUCTS, PRODUCT_ID]
    ]
}

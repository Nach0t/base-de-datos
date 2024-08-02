import sqlalchemy

# Conexión a la base de datos
db = sqlalchemy.create_engine('sqlite:///mydb.db')

# MetaData para gestionar el esquema
metadata = sqlalchemy.MetaData()

# Definición de la tabla employee
employee = sqlalchemy.Table('employee', metadata,
    sqlalchemy.Column('Department', sqlalchemy.String),
    sqlalchemy.Column('Name', sqlalchemy.String),
    sqlalchemy.Column('Salary', sqlalchemy.Float),
    sqlalchemy.Column('Seniority', sqlalchemy.Integer),
    sqlalchemy.Column('HoursOfWorking', sqlalchemy.Integer)
)

# Definición de la tabla queso
company = sqlalchemy.Table('company', metadata,
    sqlalchemy.Column('companies', sqlalchemy.String),
    sqlalchemy.Column('JobDemands', sqlalchemy.Float),
    sqlalchemy.Column('Contry', sqlalchemy.String)
)

# Crear las tablas en la base de datos
metadata.create_all(db)

# Datos a insertar en la tabla employee
business_data = [
    {'Department': 'Marketing', 'Name': 'John', 'Salary': 50000, 'Seniority': 5, 'HoursOfWorking': 250},
    {'Department': 'Marketing', 'Name': 'Alice', 'Salary': 52000, 'Seniority': 4, 'HoursOfWorking': 240},
    {'Department': 'Marketing', 'Name': 'Bob', 'Salary': 48000, 'Seniority': 6, 'HoursOfWorking': 260},
    
    {'Department': 'Sales', 'Name': 'Jane', 'Salary': 60000, 'Seniority': 2, 'HoursOfWorking': 200},
    {'Department': 'Sales', 'Name': 'Eve', 'Salary': 62000, 'Seniority': 1, 'HoursOfWorking': 210},
    {'Department': 'Sales', 'Name': 'Frank', 'Salary': 61000, 'Seniority': 3, 'HoursOfWorking': 205},
]

programmer_data = [
    {'Department': 'Deployer', 'Name': 'Luis', 'Salary': 70000, 'Seniority': 2, 'HoursOfWorking': 200},
    {'Department': 'Deployer', 'Name': 'Ana', 'Salary': 71000, 'Seniority': 3, 'HoursOfWorking': 210},
    {'Department': 'Deployer', 'Name': 'Carlos', 'Salary': 65000, 'Seniority': 2, 'HoursOfWorking': 220},
    
    {'Department': 'Backend', 'Name': 'Ea', 'Salary': 85000, 'Seniority': 5, 'HoursOfWorking': 220},
]

# Datos a insertar en la tabla queso
company_data = [
    {'companies': 'Coca Cola','Contry': 'USA', 'JobDemands': 4},
    {'companies': 'Microsoft','Contry': 'USA', 'JobDemands': 2},
    {'companies': 'Movistar','Contry': 'Chile', 'JobDemands': 2}
]

# Insertar datos en la tabla employee
with db.connect() as conn:
    with conn.begin():  # Inicia una transacción
        for data in business_data + programmer_data:
            try:
                insert_stmt = employee.insert().values(**data)
                conn.execute(insert_stmt)
            except Exception as e:
                print(f'Error inserting data into employee: {e}')
        
        # Insertar datos en la tabla company
        for data in company_data:
            try:
                insert_stmt = company.insert().values(**data)
                conn.execute(insert_stmt)
            except Exception as e:
                print(f'Error inserting data into queso: {e}')

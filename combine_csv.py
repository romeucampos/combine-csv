import duckdb # pip install duckdb

#set working directory
path = rf"/mydir" 

# csv or parquet
extension = "csv" 
# use "distinct" for unique rows, leave "" for all rows
distinct = "distinct" 

duckdb.sql(f"""
    copy (
        select {distinct} *
        from read_{extension}_auto('{path}/*.{extension}', union_by_name=true)   
    ) to 'combined_{extension}.{extension}'
""")

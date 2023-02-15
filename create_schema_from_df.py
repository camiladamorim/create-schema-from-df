import pandas as pd


TABLE_NAME="my_table"
DF_PATH = "/home/my_name/my_df.csv"


def get_data_type(data):
    try:
        data/1
        if '.' in str(data):
            return 'float'
        return 'int'
    except:
        return('varchar')


def create_table_schema():
    df=pd.read_csv(DF_PATH)
    columns=df.columns
    new_columns=[]
    for i in columns:
        new_columns.append(i.lower())
    columns=new_columns
    columns = [*set(columns)] #remove possible duplicates
    sample=df.iloc[1,:]
    chunk=""
    for i in range(len(columns)):
        chunk=chunk+columns[i].replace(" ", "_").lower() +" "+str(get_data_type(sample[i]))+", "
        chunk=chunk.replace("(", "_")
        chunk=chunk.replace(")", "")
        chunk=chunk.replace(":", "")
        chunk=chunk.replace(".", "_")
        chunk=chunk.replace("-", "_")
    query="create table " + TABLE_NAME + " (" + chunk[:-1] + ");"
    query="select * from " + TABLE_NAME + ";"
    return(query)
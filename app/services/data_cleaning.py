import pandas as pd

async def get_unique_values(df:pd.DataFrame):
  unique_values:dict[str:list] = {}
  columns:list = df.columns.tolist()
  for column in columns:
    unique_values[column] = df[column].unique.tolist()
  return unique_values
import pandas as pd

def aggregate_columns(df: pd.DataFrame, groupby_column: str = 'name', aggregate_column: str = 'data_collection') -> pd.DataFrame:
    # make sure the columns are in the dataframe
    assert groupby_column in df.columns, f'"groupby_column", {groupby_column}, ''does not appear to be in the input ''DataFrame columns.'
    assert aggregate_column in df.columns, f'"aggregate_column", {aggregate_column}, ''does not appear to be in the input ''DataFrame columns.'
    
    # create aggregated dataframe
    agg_df = df.groupby(groupby_column).aggregate({aggregate_column: list})
    
    # create a dataframe of values without the aggregation column ready to join
    df_alias = 	df.drop(columns=aggregate_column).\
                set_index(groupby_column)
    # join the aliases on and clean up the result
    out_df = agg_df.join(df_alias).\
            reset_index(groupby_column).\
            drop_duplicates(groupby_column).\
            reset_index(drop=True)
    return out_df
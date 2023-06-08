import os
import pandas as pd

SOURCE_URL = 'https://www.nifc.gov/fire-information/statistics/prescribed-fire'
LABEL_IDX = [0,2,3,4,5,6,7,8]

def get_source_data( source_url ):
    df_list = pd.read_html(source_url)
    df = df_list[0]
    labels = df_list[0].iloc[1].values
    return df, labels

def get_df_label_slice( df, key ):
    return df[df[1] == key].values

def create_df( data, labels, label_idx ):
    return pd.DataFrame(data[:,label_idx], columns=labels[label_idx])

def format_data_from_url( source_url, label_idx ):
    source_df, labels = get_source_data(source_url)
    num_data = get_df_label_slice(source_df,'Fires')
    acre_data = get_df_label_slice(source_df,'Acres')
    num_df = create_df(num_data,labels,label_idx)
    acre_df = create_df(acre_data,labels,label_idx)
    return num_df, acre_df

def save_data( num_df, acre_df, file_path='./data/' ):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    num_df.to_csv(os.path.join(file_path,'fires.csv'),index=False)
    acre_df.to_csv(os.path.join(file_path,'acres.csv'),index=False)

def main():
    num_df, acre_df = format_data_from_url(SOURCE_URL, LABEL_IDX)
    save_data(num_df, acre_df)

if __name__ == "__main__":
    main()
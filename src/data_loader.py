import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    features = df.drop(columns=['name', 'status'])
    labels = df['status']
    return features, labels

def load_data(filepath):
    import pandas as pd
    
    # Load the dataset from a CSV file
    data = pd.read_csv(filepath)
    
    # Assuming the last column is the label and the rest are features
    features = data.iloc[:, :-1].values
    labels = data.iloc[:, -1].values
    
    return features, labels
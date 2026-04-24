import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():
    df = pd.read_csv("ocean_waste.csv")
    
    le = LabelEncoder()
    
    df["Waste_Type"] = le.fit_transform(df["Waste_Type"])
    df["Area_Type"] = le.fit_transform(df["Area_Type"])
    df["Pollution_Level"] = le.fit_transform(df["Pollution_Level"])
    
    return df, le
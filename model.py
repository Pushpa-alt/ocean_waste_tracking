from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def train_model(df):
    X = df[["Waste_Type", "Quantity", "Area_Type"]]
    y = df["Pollution_Level"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    return model
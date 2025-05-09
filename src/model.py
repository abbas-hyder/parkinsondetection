from xgboost import XGBClassifier

def train_model(x_train, y_train):
    model = XGBClassifier()
    model.fit(x_train, y_train)
    return model

def predict(model, x_test):
    return model.predict(x_test)

from sklearn.preprocessing import MinMaxScaler

def scale_features(features):
    scaler = MinMaxScaler((-1, 1))
    features_scaled = scaler.fit_transform(features)
    return features_scaled

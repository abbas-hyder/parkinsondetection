from src.data_loader import load_data
from src.preprocessing import scale_features
from src.model import train_model, predict
from src.evaluation import evaluate_model
from sklearn.model_selection import train_test_split
from src.evaluation import plot_confusion_matrix
from src.evaluation import evaluate_model, show_confusion_matrix, show_classification_report

def main():
    features, labels = load_data("data/parkinsons.data")
    features_scaled = scale_features(features)
    
    x_train, x_test, y_train, y_test = train_test_split(
        features_scaled, labels, test_size=0.2, random_state=7
    )
    
    model = train_model(x_train, y_train)
    predictions = predict(model, x_test)
    
    accuracy = evaluate_model(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    

# After prediction and accuracy:
    accuracy = evaluate_model(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Show detailed evaluation
    show_confusion_matrix(y_test, predictions)
    show_classification_report(y_test, predictions)
    
# Accuracy + reports
    accuracy = evaluate_model(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    show_confusion_matrix(y_test, predictions)
    show_classification_report(y_test, predictions)

# Plot the confusion matrix
    plot_confusion_matrix(y_test, predictions)

 

if __name__ == "__main__":
    main()

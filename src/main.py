from data_visualization import load_data, data_visualization
from model_training import load_and_preprocess_data, train_model, evaluate_model
from predict import get_user_input, predict_diabetes

def main():
    print("Loading data and visualizing...")
    df = load_data()
    data_visualization(df)
    
    print("Training model...")
    X_train, X_test, y_train, y_test = load_and_preprocess_data()
    model = train_model(X_train, y_train)
    
    print("Evaluating model...")
    evaluate_model(model, X_train, y_train, X_test, y_test)

    print("\nNow, let's predict!")
    input_data = get_user_input()
    predict_diabetes(model, input_data)

if __name__ == "__main__":
    main()

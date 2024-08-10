import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

def load_data(file_path, compression=None):
    try:
        data = pd.read_csv(file_path, compression=compression)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

def prepare_data(data, threshold=30.0):
    data['distance'] = np.sqrt((data['x'] - data['x_sim'])**2 +
                                (data['y'] - data['y_sim'])**2 +
                                (data['z'] - data['z_sim'])**2)
    data['collision'] = (data['distance'] <= threshold).astype(int)
    features = ['x_sim', 'y_sim', 'z_sim', 'Vx_sim', 'Vy_sim', 'Vz_sim']
    X = data[features]
    y = data['collision']
    return X, y

def train_model(X_train, y_train):
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)

    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

    param_grid = {
        'C': [0.01, 0.1, 1, 10, 100],
        'solver': ['liblinear', 'saga']
    }
    model = GridSearchCV(LogisticRegression(class_weight='balanced', max_iter=10000), param_grid, cv=5, scoring='f1')
    model.fit(X_train_res, y_train_res)

    # Save the trained model and scaler
    import joblib
    joblib.dump(model, 'logistic_regression_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')

    return model, scaler

def evaluate_model(model, scaler, X_test, y_test):
    X_test = scaler.transform(X_test)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)

    print(f'Accuracy: {accuracy:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')
    print(f'ROC AUC Score: {roc_auc:.4f}')

    # conf_matrix = confusion_matrix(y_test, y_pred)
    # sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    # plt.xlabel('Predicted')
    # plt.ylabel('Actual')
    # plt.title('Confusion Matrix')
    # plt.show()

def predict_collision_user_input(model, scaler):
    try:
        x_sim = float(input("Enter x_sim: "))
        y_sim = float(input("Enter y_sim: "))
        z_sim = float(input("Enter z_sim: "))
        Vx_sim = float(input("Enter Vx_sim: "))
        Vy_sim = float(input("Enter Vy_sim: "))
        Vz_sim = float(input("Enter Vz_sim: "))

        input_data = pd.DataFrame({
            'x_sim': [x_sim],
            'y_sim': [y_sim],
            'z_sim': [z_sim],
            'Vx_sim': [Vx_sim],
            'Vy_sim': [Vy_sim],
            'Vz_sim': [Vz_sim]
        })

        input_data = scaler.transform(input_data)
        collision_prob = model.predict_proba(input_data)[:, 1]
        collision_prediction = (collision_prob >= 0.5).astype(int)[0]

        return collision_prediction

    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    # File paths
    train_file_path = "fl_to_int.csv.gz"  # Using GZIP-compressed training data
    test_file_path = "jan_test.csv"       # Uncompressed test data

    # Load data
    train_data = load_data(train_file_path, compression='gzip')
    test_data = load_data(test_file_path)

    if train_data is not None and test_data is not None:
        # Prepare training data
        X_train, y_train = prepare_data(train_data)
        X_test_data = test_data[['x_sim', 'y_sim', 'z_sim', 'Vx_sim', 'Vy_sim', 'Vz_sim']]

        # Train model
        model, scaler = train_model(X_train, y_train)

        # Prepare and evaluate test data
        X_test, y_test = prepare_data(train_data, threshold=30.0)  # Placeholder: Use actual test set labels if available
        evaluate_model(model, scaler, X_test, y_test)

        # Predict on the test dataset
        X_test_data = scaler.transform(X_test_data)
        collision_predictions = model.predict(X_test_data)

        # Prepare submission
        submission = pd.DataFrame({
            'id': test_data['id'],
            'collision': collision_predictions
        })
        submission.to_csv("submission.csv", index=False)

        # User input prediction
        # prediction = predict_collision_user_input(model, scaler)
        # if prediction is not None:
        #     print(f"Collision Prediction: {prediction}")

if __name__ == "__main__":
    main()

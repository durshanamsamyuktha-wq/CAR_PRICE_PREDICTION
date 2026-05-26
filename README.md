🚗 Car Price Prediction using Machine Learning
A Machine Learning project that predicts car prices based on various car features using Python and Scikit-learn.
This project includes data preprocessing, model training, testing, logging, and model saving functionalities.

📌 Project Overview
The goal of this project is to build a Machine Learning model that predicts the price of a car based on input features such as fuel type, transmission, engine details, mileage, and other specifications.

The project workflow includes:

✔ Data Loading
✔ Data Cleaning
✔ Feature Encoding
✔ Train-Test Splitting
✔ Model Training
✔ Model Evaluation
✔ Model Saving
✔ Logging and Exception Handling

🛠️ Technologies Used
Python
NumPy
Pandas
Matplotlib
Scikit-learn
Logging Module
📂 Project Structure
├── main.py
├── car_price_prediction.csv
├── main_logcode.py
├── train_logcode.py
├── testing_logcode.py
├── model_saving.py
├── logs/
└── README.md
⚙️ Features
Automatic preprocessing of categorical columns
Logging system for debugging and tracking
Modular code structure
Train/Test split implementation
Error handling using try-except
Model saving for future predictions
🚀 Project Workflow
1️⃣ Load Dataset
self.df = pd.read_csv(self.data)
2️⃣ Remove Unnecessary Columns
self.df = self.df.drop(['Car ID'], axis=1)
3️⃣ Convert Categorical Data to Numerical
All object/string columns are automatically converted into numeric values for Machine Learning processing.

4️⃣ Split Dataset
train_test_split(test_size=0.2, random_state=42)
Training Data → 80%
Testing Data → 20%
5️⃣ Train Model
obj.training()
6️⃣ Test Model
obj.testing()
7️⃣ Save Model
obj.saving_model()
▶️ How to Run the Project
Clone the Repository
git clone https:https://github.com/Narendra1306/Car_price-prediction
Navigate to Project Directory
cd car-price-prediction
Install Required Libraries
pip install -r requirements.txt
Run the Project
python main.py
📊 Machine Learning Pipeline
Dataset
   ↓
Data Preprocessing
   ↓
Feature Encoding
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Testing
   ↓
Model Saving
🧠 Concepts Used
Regression Algorithms
Data Preprocessing
Feature Engineering
Logging
Exception Handling
Model Serialization
🌐 Render Deployment Link
deployed Render link: https://car-price-prediction-1-k5xb.onrender.com

https://your-render-link.onrender.com
Example:

https://car-price-prediction.onrender.com
📈 Future Enhancements
Add Flask/Django Frontend
Hyperparameter Tuning
Deploy using Docker
Cloud Deployment
Interactive Dashboard
Real-time Prediction API
🤝 Contributing
Contributions are welcome.

Fork the repository
Create a new branch
Commit your changes
Push to the branch
Open a Pull Request
👨‍💻 Author
Developed by Muthireddy Narendra

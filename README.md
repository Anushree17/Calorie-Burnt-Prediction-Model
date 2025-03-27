# Calorie Burnt Prediction Model
<img src="https://t4.ftcdn.net/jpg/05/61/80/69/360_F_561806913_89lCAjRA3xJ2TqslsgQP7rURoBWlf6xJ.jpg" height=500 width=850>
<h2>Project Description</h2>
<p>The Calorie Burnt Prediction Model is a machine learning-based system designed to estimate the number of calories burned during a workout session. Using key physiological and activity-related parameters—gender, age, height, weight, workout duration, heart rate, and body temperature—the model predicts calorie expenditure with high accuracy. This enables individuals, fitness professionals, and healthcare providers to make data-driven decisions regarding physical activity, training intensity, and overall health managemen</p>
<h2>Use Cases</h2>
<ul>
  <li>Fitness & Wellness Apps – Personalizes workout recommendations based on predicted calorie expenditure</li>
<li>Healthcare & Rehabilitation – Assists doctors and physiotherapists in tracking patient recovery and managing obesity-related conditions.</li>
<li>Wearable Technology & Smart Devices – Enhances smartwatches and fitness trackers by providing real-time calorie burn estimates</li></ul>
  <h2>Dataset</h2>
  <ul>
    <li>ID</li>
    <li>Gender</li>
    <li>Age</li>
    <li>Height</li>
    <li>Weight</li>
    <li>Duration of the workout</li>
    <li>Heart Rate</li>
    <li>Body Temperature</li>
  </ul>
  <h2>Problem</h2>
  <p>Tracking calorie expenditure is essential for fitness and health monitoring, but existing methods often rely on inaccurate estimations or expensive wearable devices. A reliable, data-driven approach is needed to predict calorie burn using measurable physiological factors.</p>
  <h2>Approach</h2>
  <ul><li>Data Analysis: Processed a dataset with 15,000 rows and 9 columns, checking for multicollinearity using Variance Inflation Factor (VIF).</li>
<li>Feature Selection: Implemented Recursive Feature Elimination (RFE) to select the most relevant features.</li>
<li>Model Training: Developed and compared six regression models:Linear Regression (Baseline model),Lasso Regression,Random Forest Regressor,Decision Tree Regressor,XGBoost Regressor and CATBoost Regressor</li>
<li>Evaluation Metrics: Used Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² score to assess model performance, achieving 7 MSE and 0.98 R² score with XGBoost.</li>
</ul>
<h2>Impact</h2>
<ul>
  <li>Provided an accurate, data-driven alternative to predict calorie burn, reducing dependency on costly wearables.</li>
<li>Achieved a high prediction accuracy (0.98 R²), making it suitable for fitness tracking applications.</li>
<li>Demonstrated the power of machine learning in health analytics, with potential applications in fitness apps, diet planning, and personalized exercise recommendations.</li>
</ul>  
<a href="https://calorie-burnt-prediction-model.streamlit.app/">Web App Link</a>





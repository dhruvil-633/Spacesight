# [SpaceSight](https://spacesight.onrender.com): Satellite Collision Prediction Using Logistic Regression

SpaceSight is a machine learning project focused on predicting potential collisions between satellites or debris. By leveraging logistic regression, the system aims to provide an efficient and reliable method for anticipating and mitigating space collisions. This project is hosted at [SpaceSight](https://spacesight.onrender.com).

## Project Overview

- *Project Name:* SpaceSight  
- *Objective:* Predict satellite collisions using logistic regression.  
- *Technologies Used:*  
  - Python  
  - Flask (Backend)  
  - Logistic Regression (Model)  
  - HTML/CSS/JavaScript (Frontend)

## Progress Updates

### Model Development
The logistic regression model is at the core of predicting satellite collisions. The model works by analyzing historical data on satellite trajectories and debris paths to forecast potential collision events.

- *Key Components:*  
  - Data Collection: Gathering satellite trajectory data and debris information from reliable sources.  
  - Data Preprocessing: Cleaning and preparing the data for model training.  
  - Model Building: Constructing a logistic regression model to predict collisions based on various factors like speed, trajectory, and proximity.  
  - Model Evaluation: Testing the model's accuracy with training and testing datasets to ensure reliable predictions.

### Frontend Development
The frontend of SpaceSight focuses on delivering a seamless, user-friendly interface that allows users to interact with the system. The design ensures ease of use while providing detailed results in an accessible format.

- *Key Components:*  
  - Interface Design: Creating intuitive pages for users to input satellite and debris data and view results.  
  - Visualization: Displaying the predicted collision data in a clear and understandable format.  
  - Responsiveness: Ensuring that the website adapts well to different screen sizes for an optimized user experience.

### Integration
The integration phase involves connecting the logistic regression model with the frontend interface, ensuring that the user inputs flow smoothly to the model and the results are returned in real-time.

- *Key Components:*  
  - Backend Integration: Linking the Flask backend with the logistic regression model to handle predictions.  
  - Frontend-Backend Communication: Enabling seamless data flow between the frontend and backend using Flask routes and APIs.

## How to Run the Project

1. *Clone the repository:*  
   bash
   git clone https://github.com/yourusername/SpaceSight.git
   

2. *Navigate to the project directory:*  
   bash
   cd SpaceSight
   

3. *Install dependencies:*  
   bash
   pip install -r requirements.txt
   

4. *Run the Flask server:*  
   bash
   python app.py
   

5. Open the application in your browser:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Redesigned by

- *[Dhruvil Patel](https://github.com/dhruvil-633) / [LinkedIn](https://www.linkedin.com/in/dhruvil-patel-0a6b47282/)* Led the redesign of the overall system architecture and model integration to improve efficiency.  
- *[Bhavik Jobanputra](https://github.com/BhavikJobanputra) / [LinkedIn](https://www.linkedin.com/in/bhavik-jobanputra-505563289/)* Revamped the frontend design to ensure a user-friendly experience, focusing on responsiveness and interactivity.

## Contributors

- [Dhruvil Patel](https://github.com/dhruvil-633) / [LinkedIn](https://www.linkedin.com/in/dhruvil-patel-0a6b47282/) - Project Lead, Machine Learning Engineer  
- [Bhavik Jobanputra](https://github.com/BhavikJobanputra) / [LinkedIn](https://www.linkedin.com/in/bhavik-jobanputra-505563289/) - Frontend Developer  
- [Vedant Bhayani](https://github.com/VedantBhayani) / [LinkedIn](https://www.linkedin.com/in/vedant-bhayani-391122283/) - Backend Developer  
- [Manav Bachani](https://github.com/ManavBachani) / [LinkedIn](https://www.linkedin.com/in/manav-bachani-3495bb299/) - Frontend Developer  

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

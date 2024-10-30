AgriCropAdvisor - Crop Recommendation System
Introduction
Agriculture is a major source of income and employment in India. However, one of the most common challenges Indian farmers face is selecting the most suitable crop for their land. The AgriCropAdvisor project provides a data-driven solution that leverages machine learning to analyze soil and climate factors, such as temperature, humidity, rainfall, nitrogen (N), potassium (K), phosphorus (P), and pH, to recommend the optimal crops for cultivation.

Our project evaluates the performance of various machine learning algorithms to deliver personalized crop recommendations tailored to individual soil and weather conditions, enabling more effective and informed decision-making for Indian farmers.

Objective
Identify the most accurate model for recommending suitable crops based on environmental and soil conditions.
Prediction Criteria:

Soil Properties: Nitrogen (N), Phosphorus (P), Potassium (K), pH
Climate Factors: Temperature, Humidity, Rainfall
Performance Analysis
The following accuracy chart displays the performance of each evaluated model on soil and environmental data.

Accuracy Chart



Website Overview
Home Page


The AgriCropAdvisor home page welcomes users to the Crop Recommendation System, offering two main features: Crop Prediction and Crop Recommendation. A banner across the top provides helpful farming tips to guide farmers in best practices.

About Page


The "About" page explains the mission behind AgriCropAdvisor, emphasizing our goal to empower farmers with data-driven crop recommendations. By analyzing soil and weather data, we aim to support better decision-making for higher agricultural productivity.

Crop Information Page


The "Crops" page provides practical information on different crops, including images, descriptions, and essential growth tips. This feature helps farmers optimize crop care and improve yield.

Crop Prediction Page


On the Crop Prediction page, users can input soil and climate data (e.g., nitrogen, phosphorus, potassium, temperature, humidity, pH, rainfall). Based on these inputs, AgriCropAdvisor suggests the most suitable crop. A Predict Crop button submits the data, leading to the Result page. Users can return to the home page with a provided link.

Crop Prediction Result


The Crop Prediction Result page displays the predicted crop with an image. A Predict Again button allows users to re-run predictions.

Crop Recommendation Page


On the Crop Recommendation page, users input soil properties (e.g., nitrogen, phosphorus, potassium, humidity, pH) and select a state and district. The system calls the OpenWeather API to retrieve average temperature and rainfall over the past three months, which it uses to recommend crops best suited to those conditions.

Crop Recommendation Result


This page displays the recommended crops based on the specified soil and climate data for the selected location. Users can click Recommend Again to return to the Crop Recommendation page.

Conclusion
The AgriCropAdvisor Crop Recommendation System provides farmers and agricultural specialists with a robust, data-driven tool for better crop planning. By combining machine learning with climate and soil analysis, our system promotes sustainable agriculture and increased productivity, supporting a resilient food supply chain for the future.

# AgriCropAdvisor - Crop Recommendation System

## Introduction
Agriculture is a major source of income and employment in India. However, one of the most common challenges Indian farmers face is selecting the most suitable crop for their land. The **AgriCropAdvisor** project provides a data-driven solution that leverages **machine learning** to analyze soil and climate factors, such as **temperature**, **humidity**, **rainfall**, **nitrogen (N)**, **potassium (K)**, **phosphorus (P)**, and **pH**, to recommend the optimal crops for cultivation.

Our project evaluates the performance of various machine learning algorithms to deliver personalized crop recommendations tailored to individual soil and weather conditions, enabling more effective and informed decision-making for Indian farmers.

---

## Objective
- Identify the most accurate model for recommending suitable crops based on environmental and soil conditions.

**Prediction Criteria:**
- **Soil Properties:** Nitrogen (N), Phosphorus (P), Potassium (K), pH
- **Climate Factors:** Temperature, Humidity, Rainfall

---

## Performance Analysis
The following accuracy chart displays the performance of each evaluated model on soil and environmental data.

**Accuracy Chart**

![Accuracy Chart](https://github.com/user-attachments/assets/3599ddf5-d608-4285-b064-070f74f1c8fa)

---

## Website Overview

### Home Page
![Home Page](https://github.com/user-attachments/assets/78872160-381a-42b6-8e73-7c6f568e94b4)

The AgriCropAdvisor home page welcomes users to the **Crop Recommendation System**, offering two main features: **Crop Prediction** and **Crop Recommendation**. A banner across the top provides helpful farming tips to guide farmers in best practices.

### About Page
![About Page](https://github.com/user-attachments/assets/ef7c8894-7247-437a-8e4f-bad631f8847c)

The "About" page explains the mission behind AgriCropAdvisor, emphasizing our goal to empower farmers with **data-driven crop recommendations**. By analyzing soil and weather data, we aim to support better decision-making for higher agricultural productivity.

### Crop Information Page
![Crop Page](https://github.com/user-attachments/assets/faa8ee70-b34b-4c71-a914-603cbbe6aa65)

The "Crops" page provides practical information on different crops, including images, descriptions, and essential growth tips. This feature helps farmers optimize crop care and improve yield.

### Crop Prediction Page
![Crop Prediction Page](https://github.com/user-attachments/assets/788dcc33-c1d3-4163-ac33-d28c35c1e1d8)

On the Crop Prediction page, users can input soil and climate data (e.g., **nitrogen, phosphorus, potassium, temperature, humidity, pH, rainfall**). Based on these inputs, AgriCropAdvisor suggests the most suitable crop. A **Predict Crop** button submits the data, leading to the **Result page**. Users can return to the home page with a provided link.

### Crop Prediction Result
![Crop Prediction Result](https://github.com/user-attachments/assets/34bed60f-da47-43c5-a552-f5acb2373b53)

The Crop Prediction Result page displays the predicted crop with an image. A **Predict Again** button allows users to re-run predictions.

### Crop Recommendation Page
![Crop Recommendation Page](https://github.com/user-attachments/assets/14799214-e904-4c36-8a42-2a612056ffc6)

On the Crop Recommendation page, users input soil properties (e.g., **nitrogen, phosphorus, potassium, humidity, pH**) and select a **state** and **district**. The system calls the **OpenWeather API** to retrieve average temperature and rainfall over the past three months, which it uses to recommend crops best suited to those conditions.

### Crop Recommendation Result
![Crop Recommendation Result](https://github.com/user-attachments/assets/02b281e7-9ad5-41d9-a79c-58f72ef577fc)

This page displays the recommended crops based on the specified soil and climate data for the selected location. Users can click **Recommend Again** to return to the Crop Recommendation page.

---

## Conclusion
The AgriCropAdvisor Crop Recommendation System provides farmers and agricultural specialists with a robust, data-driven tool for better crop planning. By combining machine learning with climate and soil analysis, our system promotes **sustainable agriculture** and increased productivity, supporting a resilient food supply chain for the future.

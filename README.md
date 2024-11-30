# Web Scraper Project

This repository contains the code for a web scraper application, divided into two main components:  
- **Frontend**: Developed with React, located in the `FrontEnd-React` branch.  
- **Backend**: Built using Flask, located in the `BackEnd-Flask` branch.  

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Branches](#branches)
4. [Setup Instructions](#setup-instructions)
   - [Frontend Setup](#frontend-setup)
   - [Backend Setup](#backend-setup)
5. [Usage](#usage)

## Project Overview
This project enables users to scrape data from websites, process it on the backend, and visualize the results on the frontend.  

- **Frontend**: Provides an interactive user interface for scraping configurations and data visualization.  
- **Backend**: Handles the scraping logic, data processing, and serves APIs for the frontend.

---


## Branches
- **`FrontEnd-React`**: Contains all React code for the user interface.  
- **`BackEnd-Flask`**: Contains all Flask code for backend processing and APIs.  

---

## Setup Instructions

### Frontend Setup
1. Clone the repository and switch to the `FrontEnd-React` branch:  
   ```bash
   git clone -b FrontEnd-React https://github.com/jaiman25400/Web-Scraper.git
   cd web-scraper

2. Install dependencies:
   ```bash
   npm install

3. Start the development server:
   ```bash
   npm start

4. Open your browser and navigate to http://localhost:3000.

### Backend Setup
1. Clone the repository and switch to the BackEnd-Flask branch:
   ```bash
   git clone -b BackEnd-Flask  https://github.com/jaiman25400/Web-Scraper.git
   cd web-scraper

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Flask server:
   ```bash
   flask run

5. The backend will run at http://localhost:5000.

### Usage
Start both the frontend and backend servers.
Navigate to the frontend application in your browser.
Configure the scraping parameters using the UI.
View the scraped data and visualizations.

   
   
   







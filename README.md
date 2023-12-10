# Institutional Benchmarking Model

## Project Overview
This project is a GUI-based application developed using PyQt5 in Python. The application aims to measure the productivity of an institution by integrating various factors such as individual ability, work type, management effort, and quality assurance. Additionally, it includes modules for quality assessment, management oversight, and risk assessment. The project also features modules for Sales and Marketing, focusing on efficiency and productivity in customer acquisition and life cycle management.

## Project Structure
| **File/Folder**               | **Description**                                               |
|---------------------------|-----------------------------------------------------------|
| `finance_gui.py`           | GUI file for the financial module.                        |
| `main_gui.py`              | Main GUI file for the entire application.                  |
| `marketing_gui.py`         | Module for Sales and Marketing.                             |
| `modules/`                 | Folder containing Python scripts for various modules.      |
| `sales_gui.py`             | GUI file for the sales module.                              |
| `sequential_gui.py`        | GUI file for sequential calculations.                       |
| `image_files/`             | Folder containing images used in the GUI.                  |
| `sequential_ui_files/`     | Folder containing UI files for sequential GUI.          |
| `todo/`                    | Folder containing files for incomplete features.           |
| `ui_files/`                | Folder containing UI files for the main application.        |


## Key Features
- **Ability Scaling:** Classifies ability into Entry, Intermediate, High, Expert with scaling factors.  
- **Work Type Scaling:** Classifies work types into Simple, Medium, High, Complex with scaling factors.  
- **Management Category:** Low touch, medium touch, high touch, premium touch with scaling factors.  
- **Quality Assurance Requirement:** Basic, Standard, High, Premium with scaling factors.  
- **Integration Limit:** Defines the limit for integrating work products (1-50).  
- **Time Period:** Set to one week by default.  
- **Quality Assessment Index:** Measures completeness, reliability, TCOQ, standardization, and reusability.  
- **Management Oversight Index:** Includes contributions to strategy, planning, expert guidance, RQM support, governance, and people development.  
- **Risk Assessment Module:** Identifies and assesses risks based on categories, types, probability, impact, and mitigation options.  

### Quality Assessment Application
- Calculates quality assessment effort based on job type, ability, and work type.
- Applies base QA effort to calculate one QA unit.

### Management Oversight Application
- Calculates management oversight effort based on strategy, planning, guidance, RQM support, governance, and people development.
- Applies base management effort to calculate one management unit.

### Risk Assessment Application
- Identifies risk categories, types, and assesses probability, impact, and mitigation options.
- Calculates risk units based on risk impact, mitigation options, and NPV.

### Sales and Marketing Module
- Measures efficiency and productivity in customer acquisition and life cycle management.
- Includes parameters such as revenue growth, customer retention, renewal rate, sales staff distribution, marketing spends, customer success spend, and more.

### Digital Marketing Metrics
- Provides key metrics for digital marketing, including website traffic, sessions, average session duration, page views, conversion rates, and ROI.
- Analyzes various sources such as organic search, direct visitors, referrals, and social media.

## Dependencies
- `Python 3.x`  
- `PyQt5`

## Team Members
- [Rishav Aich](mailto:aich.1@iitj.ac.in)
- [Tanish Pagaria](mailto:pagaria.2@iitj.ac.in)  

(IIT Jodhpur Undergraduates)
# HealthCare Hospital Readmission - Data Quality Workflow

A comprehensive automated data quality monitoring and ETL pipeline built with n8n for healthcare hospital readmission data management.

## 📋 Project Overview

This project implements an automated data quality assurance workflow that monitors, validates, and reports on critical healthcare data from a PostgreSQL database. The system uses a scheduled trigger to run data quality checks, identify issues, load validated data, and send automated notifications.

## 🎯 Objectives

- **Data Extraction**: Extract customer revenue summaries from transactional data
- **Data Validation**: Identify and flag data quality issues (missing emails, suspicious payments)
- **Data Loading**: Load validated data into a customer revenue summary table
- **Issue Tracking**: Maintain a comprehensive data quality issues log
- **Alerting**: Send automated email reports when data quality issues are detected
- **AI-Powered Analysis**: Use AI to summarize and analyze data quality issues

## 🏗️ Architecture

### Workflow Components

#### 1. **Schedule Trigger**
- Runs every 4 hours
- Initiates the entire data quality workflow

#### 2. **Data Extraction**
- **Extract Node**: Aggregates customer data with total payment amounts
- SQL Query: Joins customer and payment tables for revenue analysis

#### 3. **Data Validation**
Two parallel data quality checks:
- **DQ – Missing Emails**: Identifies customers with null or empty email addresses
- **DQ – Suspicious Payments**: Flags payments outside normal range (≤ 0 or > 100)

#### 4. **Data Loading**
- **Load Node**: Inserts validated customer revenue summaries into `customer_revenue_summary` table
- Updates timestamp for tracking

#### 5. **Issue Recording**
- **Add Issue to DQ table**: Logs missing email issues to `data_quality_issues` table
- **Insert Sus Email to DQ**: Logs suspicious payment issues to `data_quality_issues` table

#### 6. **Issue Counting**
- **Count Issue 1:Email**: Counts missing email records
- **Count Issue :Payment**: Counts suspicious payment records

#### 7. **Conditional Alert**
- **If Node**: Checks if issue counts exceed threshold (> 0)
- Triggers email notification when issues are detected

#### 8. **Notifications**
- **Send a message**: Sends email alert with issue count via Gmail
- **Email DQ Summary**: Sends daily data quality summary with AI-generated insights

#### 9. **AI Analysis**
- **Get Recent DQ Issues**: Retrieves issues from past 24 hours (limit: 200 records)
- **AI Summarize Issues**: Uses Ollama (llama3 model) to generate intelligent summaries of data quality issues

## 🗄️ Database Schema

### Required Tables

#### `customer`
```sql
- customer_id (PK)
- first_name
- last_name
- email

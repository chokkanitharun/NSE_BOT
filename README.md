# NSEBot: Automated Report Retrieval

### 🌟 **Project Overview**
NSEBot is a robust solution for automating the retrieval of daily reports from the National Stock Exchange (NSE). This repository contains a Selenium script (`main.py`) for automating the report download process and a Streamlit application (`stream.py`) for user-friendly interactions and monitoring.

---

### 📊 **Project Goals**
1. Automate daily report retrieval from NSE using Selenium.
2. Ensure duplicate handling and validate downloaded reports for consistency.
3. Implement error-resilient operations with retry mechanisms.
4. Provide a user-friendly interface via Streamlit for monitoring and management.

---

### 🔧 **Modules Overview**

#### 1. **Selenium Script (`main.py`)**
- Automates connecting to the NSE website.
- Handles report downloads with secure data transfer.
- Validates reports for proper CSV format.

#### 2. **Streamlit Application (`stream.py`)**
- Provides a web-based interface for:
  - Monitoring download progress.
  - Viewing logs and error details.
  - Managing downloaded reports.
- Enables user interactions such as initiating or retrying downloads.

#### 3. **Duplicate Handling**
- Automatically detects and handles duplicate files.
- Renames or skips duplicates as required.

#### 4. **Error Resilience**
- Manages download failures with retry mechanisms.
- Logs errors and ensures uninterrupted operations.

#### 5. **Report Management**
- Organizes downloaded reports into structured directories.
- Provides timely notifications and updates.

---

### ⏳ **Timeline**

#### **Week 1-2: Selenium Integration and Duplicate Handling**
- Develop Selenium script for automating downloads.
- Implement duplicate detection and renaming logic.
- Validate CSV file integrity.

#### **Week 3-4: Streamlit Integration and Error Handling**
- Build Streamlit application for user-friendly interactions.
- Implement error logging and retry mechanisms in both scripts.

#### **Week 5-6: Report Management and Notifications**
- Organize downloaded reports into directories.
- Add notifications for download status and error alerts.

#### **Week 7-8: Review, Bug Fixes, and Documentation**
- Conduct a thorough review of scripts and application.
- Fix bugs and finalize features.
- Prepare comprehensive project documentation.

---

### 🎯 **How to Use**

#### Prerequisites:
1. Install Python (version 3.8 or higher).
2. Install required libraries using:
   ```bash
   pip install -r requirements.txt
   ```

#### Running the Selenium Script:
1. Navigate to the project directory.
2. Run the script to start downloading reports:
   ```bash
   python main.py
   ```

#### Launching the Streamlit Application:
1. Navigate to the project directory.
2. Start the Streamlit application:
   ```bash
   streamlit run stream.py
   ```
3. Open the provided URL in your browser to access the interface.

#### Logs and Reports:
- Logs are saved in the `logs/` directory for activity tracking and error debugging.
- Downloaded reports are stored in the `reports/` directory.

---

### 🚀 **Expected Outcomes**
1. A fully automated report retrieval system powered by Selenium.
2. Streamlined user interface for monitoring via Streamlit.
3. Reliable duplicate detection and error handling.
4. Organized and accessible report management.
5. Notifications for real-time updates and alerts.

---

### 🛠️ **Tools & Technologies**
- **Programming Language:** Python
- **Automation Framework:** Selenium
- **Web Interface:** Streamlit
- **Libraries:** Pandas, Requests, Logging, Streamlit
- **Environment:** Windows/Linux

---


---

### 🎨 **Visual Enhancements**
- 🌐 Intuitive web interface for user interactions.
- 📂 Organized directories for easy file access.
- 📝 Comprehensive logging for detailed activity tracking.

Happy Automating! 🚀


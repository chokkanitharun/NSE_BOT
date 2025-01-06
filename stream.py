import streamlit as st
from main import logic
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime, timedelta
import threading
import time

# Function to send email notification with attachment
import re  # Import regex module

def send_email_notification(user_email):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        sender_email = "tharun16c@gmail.com"
        sender_password = "bifl mtjw elzf uewb"
        server.login(sender_email, sender_password)

        subject = "Download Completed"
        body = "Your requested download has been completed successfully."

        log_file_path = r"D:\\selenium_down\\script_log.log"
        total_files = 0
        downloaded_files = 0

        if os.path.exists(log_file_path):
            try:
                with open(log_file_path, "r") as log_file:
                    logs = log_file.readlines()

                for line in logs:
                    # Use regex to find the numbers in the relevant lines
                    if "Found" in line and "download links" in line:
                        match = re.search(r"Found (\d+) download links", line)
                        if match:
                            total_files = int(match.group(1))

                    if "All" in line and "files downloaded" in line:
                        match = re.search(r"All (\d+) files downloaded", line)
                        if match:
                            downloaded_files = int(match.group(1))

                body += f"\n\nSummary:\nTotal Files Found: {total_files}\nDownloads Completed: {downloaded_files}\n\nPlease find the log file attached."
            except Exception as e:
                body += f"\n\nCould not parse the log file for summary information. Error: {e}"

            with open(log_file_path, 'rb') as log_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(log_file.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(log_file_path)}'
            )
        else:
            body += "\n\nLog file not found. No attachment is included."

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = user_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if os.path.exists(log_file_path):
            msg.attach(part)

        server.sendmail(sender_email, user_email, msg.as_string())
        server.quit()
        st.success(f"Notification sent to {user_email}!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")



# Function to check and send email after the specified time
def email_scheduler(notification_time, user_email):
    while True:
        current_time = datetime.now().time()
        if current_time >= notification_time:
            send_email_notification(user_email)
            break
        time.sleep(10)  # Check every 10 seconds

# Custom CSS for UI styling
st.markdown("""
    <style>
        .stApp { 
            background-image: url('https://t3.ftcdn.net/jpg/06/66/71/80/360_F_666718031_NjfdIITNjDQzx04ZPRSObOZygqnwaw5Z.jpg');  /* Set your background image URL */
            background-size: cover;
            background-position: center center;
            color: white;
        }
        .stButton button { 
            background-color: #A64D79; 
            color: white; 
            border-radius: 8px; 
            font-weight: bold;  /* Making the button text bolder */
            border: 3px solid #6A1E55; /* Thicker border for button */
        }
            .st-emotion-cache-qcpnpn{
            border:5px solid white;
             box-shadow: 0 0 15px 5px white;
             background-color:rgba(255,255,255,0.2);
             }

            .st-emotion-cache-ysk9xe p {
            font-size:20px;
           
           background-color:rgb(6, 3, 37) !important;}

            .st-emotion-cache-1y5f4eg p {
    word-break: break-word;
            font-size:20px;
            background-color:rgb(6, 3, 37) !important;
             box-shadow: 0 0 15px 5px white;
}
        .stButton button:hover { 
            background-color: #6A1E55; 
            border: 3px solid #A64D79; /* Thicker border on hover */
        }
        .header { 
            text-align: center; 
            font-size: 24px; 
            color: #F4D9D0; 
            background-color: #C75B7A; 
            padding: 10px; 
            border-radius: 8px; 
            margin-bottom: 20px;
            font-weight: bold; 
        }
        .info-box { 
            text-align: center; 
            margin: 10px auto; 
            padding: 10px; 
            background-color: #F4D9D0; 
            color: #C75B7A; 
            font-size: 18px; 
            border-radius: 8px; 
            font-weight: bold;  /* Bolder font for info box */
        }
        .form-container {
            width: 80%;
            margin: auto;
            padding: 20px;
            background-color: #FFFFFF;
            border-radius: 8px;
            border: 3px solid #A64D79; /* Thicker border */
            box-shadow: 0 0 15px 5px #A64D79;
        }
        .stTextInput input, .stTextInput label {
            font-weight: bold;  /* Making form inputs bolder */
            border: 3px solid #A64D79; /* Thicker border for input fields */
            box-shadow: 0 0 15px 5px #A64D79 ; 
            background-color:rgb(6, 3, 37);
            border-radius: 10px;
            padding: 10px;
            
            
        }
        .stTextInput input:focus {
            border-color: #6A1E55;  /* Change border color on focus */
        }
        .stTextInput input {
            background-color: #6A1E55;  /* Set pink background color */
        }
        /* Make the label text bolder */
        .stTextInput label {
            font-weight: bold;
            font-size:20px;
        }
         .stWarning {
    background-color:rgb(6, 3, 37) !important; 
    color: #6A1E55 !important; /* Ensure text remains white */
    border: 2px solid #1A1A1D;
    border-radius:5px;
}

    </style>
""", unsafe_allow_html=True)

# Main Streamlit app
def app():
    st.markdown('<div class="header">NSE Automated Report Downloader</div>', unsafe_allow_html=True)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f'<div class="info-box">Current Date and Time: {current_time}</div>', unsafe_allow_html=True)

    # Initialize session state for download completion
    if "download_completed" not in st.session_state:
        st.session_state.download_completed = False

    with st.form("user_form"):
        user_time_str = st.text_input("Enter Notification Time (HH:MM format):", placeholder="e.g., 14:30", help="Specify the time in 24-hour format for receiving notifications.")
        user_email = st.text_input("Enter your email address to receive the notification:", placeholder="example@domain.com")

        submitted = st.form_submit_button("Download Data")

        if submitted:
            if user_email and user_time_str:
                try:
                    user_time = datetime.strptime(user_time_str, "%H:%M").time()
                    current_time = datetime.now().time()

                    # Start the download process
                    with st.spinner("Download started..."):
                        try:
                            result = logic()  # Call the logic function to start the download
                            st.success(result)  # Notify when the download is complete
                            st.session_state.download_completed = True  # Set the flag to True
                        except Exception as e:
                            st.error(f"An error occurred: {e}")

                    # Schedule email notification
                    st.info("Email notification will be sent when the time is reached.")
                    notification_thread = threading.Thread(target=email_scheduler, args=(user_time, user_email), daemon=True)
                    notification_thread.start()

                except ValueError:
                    st.error("Invalid time format. Please enter the time in HH:MM format.")
            else:
                st.error("Please fill out all fields correctly.")

    # View Logs Button
    log_file_path = r"D:\\selenium_down\\script_log.log"
    if st.session_state.download_completed and os.path.exists(log_file_path):
        if st.button("View Logs"):
            try:
                with open(log_file_path, "r") as log_file:
                    logs = log_file.read()
                    st.text_area("Log File Contents:", logs, height=300)
            except Exception as e:
                st.error(f"Unable to read log file: {e}")
    elif not st.session_state.download_completed:
        st.warning("Logs will be available after the download process is completed.")
    elif not os.path.exists(log_file_path):
        st.warning("Log file not found.")

if __name__ == "__main__":
    app()

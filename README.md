# Upwind Assignments

## Description:
This repository contains three assignments:  
1. **Phishing Email Detection**  
2. **Malware Analysis in an Isolated Environment**  
3. **SQL Injection Simulation and Prevention**  


## Assignment 1 – Phishing Email Detection

Built a Python script that analyzes the text of an email and determines if it is potentially a phishing attempt.  

Detection was based on:  
1. **Urgent Words** – Detects common urgency phrases like `"urgent"`, `"immediately"`, `"act now"`.  
2. **Suspicious IPs & URLs** – Extracts and checks IPs/URLs against a trusted domain list.  
3. **Sender Legitimacy** – Validates the sender’s domain to ensure it matches the claimed organization.  

After running these checks, the script:  
- Labels the email as **"Phishing"** or **"Not Phishing"**.  
- Provides a short reason summary if phishing is detected.  

### How to run
```bash
python phishing_detector.py email.txt
```



## Assignment 2 – Malware Analysis in an Isolated Environment

Built a Docker-based isolated environment to safely execute and analyze suspicious scripts.  

The "malware" script performed:  
1. **Opening a file** 
2. **Creating a network connection** 
3. **Creating a child process using os.system**

We monitored the malware behavior using the strace command to see system calls and detect what changes it made.

### How to run
```bash
# Build the Docker image
docker build -t malware-sandbox .
```
```bash
#  Run the malware in an isolated container and capture behavior
docker run --rm -v "${PWD}:/app" malware-sandbox sh -c "strace -f -o /app/trace.log python -u /app/malware.py"

```

## Assignment 3 – SQL Injection Simulation and Prevention

- Created a simple Flask web application with:  
  - A login form (`login.html`).  
  - A SQLite database containing one user (`admin`, `admin123`).  

- **Vulnerable Version (`app.py`)**:  
  - Built a login system with insecure string-based SQL queries.  
  - Demonstrated SQL injection using: `' OR '1'='1` which allowed login without valid credentials.  

- **Secure Version (`app_secured.py`)**:  
  - Used parameterized queries to prevent SQL injection.  
  - Attempted the same injection and confirmed login fails.  

### How to run

1. Install dependencies:
    ```bash
    pip install flask
    python new_db.py  # Create database and sample user
    ```

2. Run vulnerable app:
    ```bash
    python app.py
    ```
    Test the vulnerable login:  
    Open the app in your browser (usually at **http://127.0.0.1:5000**).  
    Log in with:  
    - **Username:** admin  
    - **Password:** admin123  

    → You should see **"Login successful"**.  

    Try an SQL injection attack:  
    - **Username:** any value (e.g., test)  
    - **Password:** `'1'='1`  

    → You will still see **"Login successful"** (vulnerability confirmed).  

3. Run secure app:
    ```bash
    python app_secured.py
    ```
    Try the same valid credentials (**admin / admin123**) → should succeed.  

    Try the SQL injection attack (`'1'='1`) → login should fail, proving the mitigation works.  



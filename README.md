Basic Phishing Awareness Simulation (Flask)

This is a simple phishing awareness simulation built using Python and Flask.
The purpose of this project is to understand how phishing login pages work and how user credentials can be captured in insecure systems.

This project is created only for educational and defensive learning purposes.

___________________________________________________________________________

What This Project Does

- Creates a fake login page using HTML
- Accepts username and password input
- Stores submitted credentials in a local file (captured.txt)
- Runs on localhost (127.0.0.1) only

___________________________________________________________________________

Technologies Used

- Python
- Flask
- HTML
- Basic file handling

___________________________________________________________________________

Project Structure

```
basic-phishing-simulation/
│
├── app.py
├── captured.txt
└── templates/
    └── login.html
```
___________________________________________________________________________

How To Run

1. Install Flask:
pip install flask

2.Run the application:
python app.py

3.Open browser and visit:
http://127.0.0.1:8000

___________________________________________________________________________

How It Works

- User enters login credentials
- Flask receives POST request
- Data is stored in captured.txt
- User is redirected back to login page

___________________________________________________________________________

Important Note

This project is developed for cybersecurity awareness and academic learning.
It should only be used in controlled environments for educational purposes.

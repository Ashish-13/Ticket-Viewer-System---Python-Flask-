# Ticket-Viewer-System-Python(Flask)

Ticket Viewer Application

Description: The application retrieves data from Zendesk API and displays them in a web-based user interface. It provides the following functionalities:
1. Search a particular ticket details using the ticket id.
2. View all tickets and then view ticket details accordingly.

Technology Used: Python (version 3.7), HTML and CSS

Web Framework: Flask, Jinja2 and Bootstrap
Python Library:
1. flask
2. flask_paginate
3. requests 
4. json 
 
Installation:
1. Install Python version 3.7 and add to the path.
2. Open Command Prompt and type "python" to check if python is installed.
3. Check if pip is present. Type “pip -V”
4. Run the following commands in the command prompt to install python libraries required:
pip install flask
pip install flask_paginate
pip install requests
pip install json

Project File Structure:

->Zendesk Ticket Viewer
	->README
	->Ticket Viewer
		-TicketViewer.py
		-template
		-static

Launching Application:
1. Open command prompt and go to the directory where TicketViewer.py file is present.
Exmaple: C:\Users\Ashish>cd "Desktop\Zendesk Ticket Viewer\Ticket Viewer"

2. Now execute the command: python TicketViewer.py
Example: C:\Users\Ashish\Desktop\Zendesk Ticket Viewer\Ticket Viewer>python TicketViewer.py

3. Press enter, and the application will launch. Copy the url displayed, paste it in the web browser or go to http://localhost:5000/
  
Usage Instruction:
1. After pasting the url in the browser you will see the home page.
2. Now it provides two options: to search a ticket using ticket id or view all tickets.
3. Enter a ticket id (integer between 1 – 100) and it will redirect you to that ticket page containing its details.
4. Click “All Tickets”  button to view all tickets.


Happy Path Test handled by the application:
1. Input Field Test:
	a. Input = Aplhanumeric or Character throws incorrect id message
	b. Input = Blank throws Please enter a value message
	c. Input = Numeric Id not present in the data throws Ticket ID does not exist message.

2. URL test:
	a. If URL= http://localhost:5000/<random-value> shows page not found.

3. API test:
	a. If API unavailable or data is empty throws API unavailable error.



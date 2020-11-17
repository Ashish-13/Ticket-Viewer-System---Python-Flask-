import requests
import json
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_paginate import Pagination, get_page_args
app = Flask(__name__, template_folder="template")

#---------------------------------------------Zendesk API--------------------------------------------------------------#

def getAPIdata():
    
    """Description : Connect to Zendesk API and retrieve data in json format.
    Returns: List of tickets with data elements in dictionary format
    """

    url = 'https://ashish1994.zendesk.com/api/v2/tickets.json'
    user = 'ashishrawat1994@gmail.com' +'/token'
    pwd = 'eL9lloVtIW1RpxFmYlZ8smtvCgRO80cVSvgUi7aA'
    response = requests.get(url, auth=(user, pwd))
    return response

#Defining global variable to store API response
resp = getAPIdata() 

#-----------------------------------------------API and Page Not Found Check------------------------------------------#
@app.route('/')
def apiCheck():
    if not resp.ok:
        return render_template('apierror.html',errorv = "API Unavailable")
    else:
        return redirect(url_for('home'))

@app.errorhandler(404)
def not_found(e):
    return render_template('apierror.html',errorv= "Page Not Found")

#------------------------------------Home Page for Tickets Viewer-----------------------------------------------------#

@app.route('/home', methods= ['POST', 'GET'])
def home():
    
    """
    Description: Home Page of Ticket Viewer Application. 
    Functionality 1: Search Ticket ID or throw error message. 
    Returns: Redirects to Ticket Details for the id enetered.

    Functionality 2: View all tickets
    Return: Redirects to all tickets page.
    """
    json_data = resp.json()['tickets']
    if request.method == 'POST':
        input_data = request.form['ticketID'] 
        if input_data == '':                                                    #Check if input is null
            return render_template('home.html', value="Please enter a value")
        elif input_data.isnumeric():                                            #Check if input is numeric as required
            if int(input_data) in [k['id'] for k in json_data]:                                      #Check if id is present
                return redirect(url_for("ticketValue", arg_a = input_data))
            else:
                return render_template('home.html', value = "Ticket ID does not exist")
        else:
            return render_template('home.html', value = "Incorrect value entered")
    else:
        return render_template('home.html')
    
     
#----------------------------------------All Tickets ------------------------------------------------------------------#

def ticketsPerPage(page, offset = 0 , per_page = 25):
    
    """ Description: Slice the ticket list and show 25 tickets per page"""
    json_data = resp.json()['tickets']
    offset = (page-1) * (25)
    return json_data[offset: offset + per_page]  

@app.route('/alltickets', methods = ['POST', 'GET'])
def getTickets():
    
    """ Description: Show all tickets in a paginated format.
    Input: Click from home page or ticket details.
    Return: display 25 tickets in one page.
    """
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    per_page = 25
    json_data = resp.json()['tickets']
    total = len(json_data)
    tickets_per_page = ticketsPerPage(page= page, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('alltickets.html', content=tickets_per_page, page=page, per_page=per_page, pagination=pagination)


#--------------------------------------------Ticket Details-------------------------------------------------------------#


@app.route("/ticketid_<arg_a>", methods= ['POST', 'GET'])
def ticketValue(arg_a, ):

    """Description: Display a ticket details. 
    Input: Accepts ticket id argument from the user.
    Returns: Details of that ticket.  
    """
    json_data = resp.json()['tickets']
    for k in json_data:
        if k['id'] == int(arg_a):
            return render_template('ticketDetails.html', tdetails = k)
        else:
            pass
    return redirect(url_for('home'))


#------------------------------------------------APP START---------------------------------------------------------------#
if __name__ == "__main__":
    app.run(debug=True)


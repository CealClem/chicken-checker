Project Title
Reminder for Community Chicken Coop

1. Table of Contents
2. Introduction
3. Dependencies
4. Installation
5. Usage
6. Configuration



Introduction

This project has two main objectives so far:
1. Remind association members of their chicken duties the next day.
2. Alert all association members when there's a gap in the calendar.

Dependencies

For querying google sheets : gspread, google.oauth2.service_account
To send emails: smtplib, email.message, ssl

Installation

You'll need to get the sheet id of the google sheet in question. You'll also need to create the credentials.json file.
I forgot how I did that but I'll fill it in later: you need to set up a service account on GCP.
Replace the variables in config.py with your own values.

Usage

You can set up a cron job to make this run every day at the same time.
For example:
In the terminal: crontab -e
Then enter: 30 17 * * * /path/to/your/script.py
This will execute the file at 17:30 every day
Press 'esc' then 'wq' to quit.

Configuration

COMING SOON

Next Steps:
Deploy this on heroku?
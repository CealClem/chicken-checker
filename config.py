from google.oauth2.service_account import Credentials
import gspread

SENDER_EMAIL = "REPLACE WITH YOUR OWN VALUES"
SENDER_PASSWORD = 'REPLACE WITH YOUR OWN VALUES'
SHEET_ID = "REPLACE WITH YOUR OWN VALUES"

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

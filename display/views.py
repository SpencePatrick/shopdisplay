from __future__ import print_function
from django.shortcuts import render

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1bw7MY3EK2GifM1h_wtYZ4VJhpHllQ6HGpCbRxPiejxs'
SAMPLE_RANGE_NAME = 'Airplane Readiness!A1:P9'
# Create your views here.

def index(request):
    store = file.Storage('./display/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('./display/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1bw7MY3EK2GifM1h_wtYZ4VJhpHllQ6HGpCbRxPiejxs'
    RANGE_NAME = 'Airplane Readiness!A1:P9'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    SPREADSHEET_ID = '1bw7MY3EK2GifM1h_wtYZ4VJhpHllQ6HGpCbRxPiejxs'
    RANGE_NAME = 'Pilot Readiness!A1:P12'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    pilotvalues = result.get('values', [])
    
    context = {'pilotvalues': pilotvalues, 'values': values}
    return render(request, 'index.html', context)

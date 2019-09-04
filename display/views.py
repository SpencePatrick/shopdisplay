from __future__ import print_function
from django.shortcuts import render
from .models import Plane, Pilot
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1bw7MY3EK2GifM1h_wtYZ4VJhpHllQ6HGpCbRxPiejxs'
SAMPLE_RANGE_NAME = 'Airplane Readiness!A1:P12'
# Create your views here.

def index(request):
    try:
        store = file.Storage('./display/token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('./display/credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))

        # Call the Sheets API
        SPREADSHEET_ID = '1bw7MY3EK2GifM1h_wtYZ4VJhpHllQ6HGpCbRxPiejxs'
        RANGE_NAME = 'Airplane Readiness!A1:P12'
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueRenderOption='FORMATTED_VALUE', dateTimeRenderOption='FORMATTED_STRING').execute()

        values = result.get('values', [])

        planes = Plane.objects.all()
        # planes is the local database cache. If it exists then I need to overwrite the cache. the data is written to db.sqlite3
        if planes.exists():
            print('plane exists')
            index = 0
            number = ''
            for value in values:
                if value[1] == 'N6993N':
                    number = '93N'
                elif value[1] == "N114BH":
                    number = "4BH"
                elif value[1] == 'N732DW':
                    number = "2DW"
                if len(value[1]) > 3:
                    plane = Plane.objects.get(nnumber=value[1])
                    plane.aircraftstatus = value[14]
                    plane.discrepancies =value[15]
                    if value[14] == "LOADING...":
                        value[14] = plane.aircraftstatus
                    if value[0] == "#ERROR!":
                        value[14] = plane.aircraftstatus
                else:
                    plane = Plane.objects.get(nnumber=number)
                    plane.aircraftstatus = ''
                    plane.discrepancies =''
                if value[0] == "#ERROR!":
                    value[0] = plane.color
                if value[0] == "LOADING...":
                    value[0] = plane.color
                plane.color=value[0]
                plane.lasttach=value[2]
                plane.currenttach=value[3]
                plane.lastflight =value[4]
                plane.recordsreview = value[5]
                plane.annualdue = value[6]
                plane.fiftyhourdue = value[7]
                plane.hundredhourdue = value[8]
                plane.transponderdue = value[9]
                plane.phaseone = value[10]
                plane.phasetwo = value[11]
                plane.phasethree = value[12]
                plane.phasefour = value[13]
                plane.save()
                index = index + 1
            print('Planes cache has been updated')
        else:
            # If the planes cache does not exist,
            index = 0
            number = ''
            for value in values:
                if value[1] == 'N6993N':
                    number = '93N'
                elif value[1] == "N114BH":
                    number = "4BH"
                elif value[1] == 'N732DW':
                    number = "2DW"
                print(number)
                if value[0] != '':
                    plane = Plane(
                        color=value[0],
                        nnumber=value[1],
                        lasttach=value[2],
                        currenttach=value[3],
                        lastflight =value[4],
                        recordsreview = value[5],
                        annualdue = value[6],
                        fiftyhourdue = value[7],
                        hundredhourdue = value[8],
                        transponderdue = value[9],
                        phaseone = value[10],
                        phasetwo = value[11],
                        phasethree = value[12],
                        phasefour = value[13],
                        aircraftstatus = value[14],
                        discrepancies =value[15]
                    )
                    plane.save()
                else:

                    plane = Plane(
                        color=value[0],
                        nnumber=number,
                        lasttach=value[2],
                        currenttach=value[3],
                        lastflight =value[4],
                        recordsreview = value[5],
                        annualdue = value[6],
                        fiftyhourdue = value[7],
                        hundredhourdue = value[8],
                        transponderdue = value[9],
                        phaseone = value[10],
                        phasetwo = value[11],
                        phasethree = value[12],
                        phasefour = value[13],
                        aircraftstatus ='',
                        discrepancies =''
                    )
                    print(plane)
                    plane.save()
                index = index + 1
        SPREADSHEET_ID = '1bw7MY3EK2GifM1h_wtYZ4VJhpHllQ6HGpCbRxPiejxs'
        RANGE_NAME = 'Pilot Readiness!A1:P15'
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, dateTimeRenderOption='FORMATTED_STRING').execute()
        pilotvalues = result.get('values', [])
        pilots = Pilot.objects.all()
        if pilots.exists():
            print('pilot exists')
            for value in pilotvalues:
                pilot = Pilot.objects.get(name=value[0])
                pilot.title=value[1]
                pilot.cert=value[2]
                pilot.certnumber=value[3]
                pilot.medicaldue =value[4]
                pilot.medicalclass = value[5]
                pilot.faase = value[6]
                pilot.faame = value[7]
                pilot.faainst = value[8]
                pilot.faainsttype = value[9]
                pilot.opsapproved = value[10]
                pilot.acapproved = value[11]
                pilot.daycurrency = value[12]
                pilot.nightcurrency = value[13]
                pilot.checkairman = value[14]
                pilot.save()
        else:
            print('pilot doesnt exist')
            for value in pilotvalues:

                pilot = Pilot(
                    name=value[0],
                    title=value[1],
                    cert=value[2],
                    certnumber=value[3],
                    medicaldue =value[4],
                    medicalclass = value[5],
                    faase = value[6],
                    faame = value[7],
                    faainst = value[8],
                    faainsttype = value[9],
                    opsapproved = value[10],
                    acapproved = value[11],
                    daycurrency = value[12],
                    nightcurrency = value[13],
                    checkairman = value[14]
                )

                pilot.save()
        print('here we are')
        context = {'pilotvalues': pilotvalues, 'values': values}
        return render(request, 'index.html', context)
    except Exception as e:
        pilotvalues = Pilot.objects.all().values()
        planevalues = Plane.objects.all().values()
        planes = []
        for item in planevalues:
            plane = [
                item['color'],
                item['nnumber'],
                item['lasttach'],
                item['currenttach'],
                item['lastflight'],
                item['recordsreview'],
                item['annualdue'],
                item['fiftyhourdue'],
                item['hundredhourdue'],
                item['transponderdue'],
                item['phaseone'],
                item['phasetwo'],
                item['phasethree'],
                item['phasefour'],
                item['aircraftstatus'],
                item['discrepancies']
            ]
            planes.append(plane)

        pilots = []
        for item in pilotvalues:
            pilot = [
                item['name'],
                item['title'],
                item['cert'],
                item['certnumber'],
                item['medicaldue'],
                item['medicalclass'],
                item['faase'],
                item['faame'],
                item['faainst'],
                item['faainsttype'],
                item['opsapproved'],
                item['acapproved'],
                item['daycurrency'],
                item['nightcurrency'],
                item['checkairman']
            ]
            pilots.append(pilot)
        print('an exception occurred')
        print(e)
        context = {'pilotvalues': pilots, 'values': planes, 'error': e}
        return render(request, 'index.html', context)

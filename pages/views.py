from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from constantOutput import logData
import json
import subprocess

tab = None
log = logData()

def home_page(request, *args, **kwargs):
    global tab

    context = {
        'data':request.POST.get("con"),
        '7_days': 'Status: down',
        'mumble': 'Status: down',
        'whoami': 'Status: down',
        'chores': 'Status: down',
        'wiki': 'Status: down',
        'traefik': 'Status: down',
        'database': 'Status: down',
    }
    

    
    tab = request.POST.get("con")

    ##context['data'] = log.getLogs(tab)
    return render(request, "index.html", context)

@csrf_exempt
def data_refresh(request, *args, **kwargs):
    global tab
    global log

    print( request.headers['cookie'] )
#   if request.method == 'POST':
#       print( request.POST )
#   if request.method == 'GET':
#       print( request.GET )
#    print( request.POST.get("csrf_token") )
    tempDict = {
            "output": "fate",
            }


    running = str(subprocess.check_output(["docker",'ps','--format',"'{{.Names}}'"],stderr=subprocess.STDOUT)).replace("'", '').replace('"','')[1:].strip().split("\\n")

#  ['chores', 'wiki', 'whoami', 'database', 'traefik', 'mumble-server', '']

    if '7_days' in running:
        tempDict['days7'] = 'up'
    else:
        tempDict['days7'] = 'down'

    if 'chores' in running:
        tempDict['chores'] = 'up'
    else:
        tempDict['chores'] = 'down'

    if 'wiki' in running:
        tempDict['wiki'] = 'up'
    else:
        tempDict['wiki'] = 'down'

    if 'whoami' in running:
        tempDict['whoami'] = 'up'
    else:
        tempDict['whoami'] = 'down'

    if 'database' in running:
        tempDict['database'] = 'up'
    else:
        tempDict['database'] = 'down'

    if 'traefik' in running:
        tempDict['traefik'] = 'up'
    else:
        tempDict['traefik'] = 'down'

    if 'mumble-server' in running:
        tempDict['mumble'] = 'up'
    else:
        tempDict['mumble'] = 'down'

    result = json.dumps( tempDict )

#========================================================================================================================    

    print( '\t\t\t\t\t\t' + tab )
    if tab == "7_Days":
        tempDict['logs'] = log.getLogs("7_Days")
    if tab == "Chores":
        tempDict['logs'] = log.getLogs("Chores")
    if tab == "Wiki":
        tempDict['logs'] = log.getLogs("Wiki")
    if tab == "Whoami":
        tempDict['logs'] = log.getLogs("Whoami")
    if tab == "Postgres":
        tempDict['logs'] = log.getLogs("Database")
    if tab == "Traefik":
        tempDict['logs'] = log.getLogs("Traefik")
    if tab == "Mumble":
        tempDict['logs'] = log.getLogs("Mumble")
    if tab == "Synapse":
        tempDict['logs'] = log.getLogs("Synapse")
    if tab == "Git":
        tempDict['logs'] = log.getLogs("Git")

        

    return JsonResponse( tempDict )

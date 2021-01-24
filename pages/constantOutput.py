import sys
import os
import subprocess
import json
import time

class logData:
    items = ["chores",'mumble-server', 'whoami', 'database', 'traefik', 'wiki']

    choreLogs = { "last":"dkdkdkdkdkdkdkdkd"}
    mumbleLogs = {"last":"dkdkdkdkdkdkdkdkd"}
    whoamiLogs = {"last":"dkdkdkdkdkdkdkdkd"}
    databaseLogs = {"last":"dkdkdkdkdkdkdkdkd"}
    traefikLogs = {"last":"dkdkdkdkdkdkdkdkd"}
    wikiLogs = {"last":"dkdkdkdkdkdkdkdkd"}

    lastChange = time.time()
    updates = list()

    def loop1():
        print( "What would you like to monitor?" )
        print( "1) Everything" )
        print( "2) chores" )
        print( "3) database" )
        print( "4) mumble-server" )
        print( "5) traefik" )
        print( "6) whoami" )
        print( "7) wiki" )

#   watch = input()

        print( "What level logs would you like to load?" )
        print( "1) All" )
        print( "2) Info" )
        print( "3) Error" )
        print( "4) Fatal" )

#   level = input()

        watch = "1"
        level = "1"

        if watch == "1":
            logEverything(level)

        if watch == "quit" or level == "quit":
            return "quit"

    def processChores( output ):
        data = output.split("\\n" )
        if data[-1] != choreLogs['last']:
            for i in data:
                choreLogs[ len(choreLogs) ] = i

                updates.append(i)

            choreLogs['last'] = data[-1]
            return "Chores have been updated!"
        return "No updates for chores"

    def processDatabase( output ):
        data = output.split("\\n" )
        if data[-1] != databaseLogs['last']:
            for i in data:
                if "LOG:" in i:
                    databaseLogs[len(databaseLogs)] = i[i.find("LOG:")+4:].strip()

            databaseLogs['last'] = data[-1]
            return "Database has been updated!"
        return "No updates for Database"

    def processMumble( output ):
        data = output.split("\\n" )
        if data[-1] != mumbleLogs['last']:
            for i in data:
                if "=>" in i:
                    mumbleLogs[len(mumbleLogs)] = i[i.find("=>")+2:].strip()

            mumbleLogs['last'] = data[-1]
            return "Mumble has been updated!"
        return "No updates for Mumble"

    def processTraefik( output ):
        data = output.split("\\n")
        if data[-1] != traefikLogs['last']:
            for i in data:
                if "level=info" in i:
                    traefikLogs[len(traefikLogs)] = i[i.find('msg="')+5:].strip()

            traefikLogs['last'] = data[-1].strip()
            return "Traefik has been updated!"
        return "No updates for Traefik"

    def processWhoami( output ):
        data = output.split("\\n")
        if data[-1] != whoamiLogs['last']:
            for i in data:
                whoamiLogs[ len(whoamiLogs) ] = i.strip()
            whoamiLogs['last'] = data[-1].strip()
            return "Whoami has been updated!"
        return ("No updates for Whoami")

    def processWiki( output ):
        data = output.split("\\n")
        if data[-1] != wikiLogs['last']:        
            for i in data:
                wikiLogs[len(wikiLogs)] = i.strip()
        
            wikiLogs['last'] = data[-1].strip()
            return( "Wiki has been updated!" )
        return("No updates for Wiki")

    def getData( container ):
        return str( subprocess.check_output(["docker",'logs',container],stderr=subprocess.STDOUT))

    def simpleTraefik():
        return getData( "traefik" )

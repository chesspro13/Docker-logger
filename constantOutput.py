import sys
import os
import subprocess
import json
import time

class logData:



    def getData( self, data):

        return str( subprocess.check_output(["docker",'logs',data],stderr=subprocess.STDOUT))
    

#   def processChores( output ):
#       data = output.split("\\n" )
#       if data[-1] != choreLogs['last']:
#           for i in data:
#               choreLogs[ len(choreLogs) ] = i

#               updates.append(i)

#           choreLogs['last'] = data[-1]
#           return "Chores have been updated!"
#       return "No updates for chores"

    def processChores( self ):
        data = self.getData('chores').split("\\n" )
        logs = ""
        for i in data:
            logs += i + '<br>'

        return logs 

#       data = output.split("\\n" )
#       if data[-1] != databaseLogs['last']:
#           for i in data:
#               if "LOG:" in i:
#                   databaseLogs[len(databaseLogs)] = i[i.find("LOG:")+4:].strip()

#           databaseLogs['last'] = data[-1]
#           return "Database has been updated!"
#       return "No updates for Database"

    def processDatabase( self ):
        print( "TODO: LOOKING FOR DATABASE THIGN")
        data = self.getData('database').split("\\n" )
        logs = ""
        for i in data:
            logs += i[i.find("LOG:")+4:].strip() + '<br>'

        return logs

#   def processMumble( output ):
#       data = output.split("\\n" )
#       if data[-1] != mumbleLogs['last']:
#           for i in data:
#               if "=>" in i:
#                   mumbleLogs[len(mumbleLogs)] = i[i.find("=>")+2:].strip()

#           mumbleLogs['last'] = data[-1]
#           return "Mumble has been updated!"
#       return "No updates for Mumble"


    def processMumble( self ):
        data = self.getData("mumble-server").split("\\n" )
        log = "" #list()
        for i in data:
            if "=>" in i:
#               log.append( i[i.find("=>")+2:].strip())
                log += ( i[i.find("=>")+2:].strip()) + '<br>'
        return log            


#   def processTraefik( output ):
#       data = output.split("\\n")
#       if data[-1] != traefikLogs['last']:
#           for i in data:
#               if "level=info" in i:
#                   traefikLogs[len(traefikLogs)] = i[i.find('msg="')+5:].strip()

#           traefikLogs['last'] = data[-1].strip()
#           return "Traefik has been updated!"
#       return "No updates for Traefik"

    def processTraefik( self ):
        data = self.getData("traefik").split('\\n')
        log = ""
        for i in data:
            log += i[i.find('msg="')+5:].strip() + '<br>'
        return log
    

#   def processWhoami( output ):
#       data = output.split("\\n")
#       if data[-1] != whoamiLogs['last']:
#           for i in data:
#               whoamiLogs[ len(whoamiLogs) ] = i.strip()
#           whoamiLogs['last'] = data[-1].strip()
#           return "Whoami has been updated!"
#       return ("No updates for Whoami")

    def processWhoami( self ):
        data = self.getData("whoami").split("\\n")
        logs = ""
        for i in data:
            logs += i.strip() + '<br>'
        return logs


#   def processWiki( output ):
#       data = output.split("\\n")
#       if data[-1] != wikiLogs['last']:        
#           for i in data:
#               wikiLogs[len(wikiLogs)] = i.strip()
#       
#           wikiLogs['last'] = data[-1].strip()
#           return( "Wiki has been updated!" )
#    return("No updates for Wiki")
    def processWiki( self ):
        data = self.getData('wiki').split("\\n")
        logs = ""
        for i in data:
            logs += i.strip() + "<br>"
        
        return logs

    def getLogs( self, container ):

        data = ""

        if container == "7_Days":
            return "Not set up yet!"
        if container == "Chores":
            return self.processChores()
        if container == "Git":
            return "Not set up yet!"
        if container == "Mumble":
            return self.processMumble()
        if container == "Database":
            return self.processDatabase()
        if container == "Synapse":
            return "Not set up yet!"
        if container == "Traefik":
            return self.processTraefik()
        if container == "Wiki":
            return self.processWiki()

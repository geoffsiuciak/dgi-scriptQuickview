#!/usr/bin/env python3

'''
assumes script is located in the relevant working dir.
usage: (nix): ./scriptQuickview
usage: (win): python3 scriptQuickview
'''

import os
import json

class quickViewer():
    def __init__(self):
        self.scripts = []
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for file in files: 
            if (file.endswith(".json")):
                with open(file, 'r') as j:
                    s = json.loads(j.read())
                    header = s["scriptHeader"]
                    self.scripts.append(
                        scriptHeader(
                            header["testId"]
                          , header["scriptName"]
                          , header["revisionNumber"]
                          , header["scriptDuration"]
                        )
                    )
    
    def dumpDetails(self):
        count = len(self.scripts)
        if (0 == count):
            print("No scripts found!")
            exit()
        else:
            print(f"found {count} scripts:\n")
            for s in self.scripts:
                s.print()

class scriptHeader():
    def __init__(self, testId, scriptName, revisionNumber, scriptDuration):
        self.testId = testId
        self.scriptName = scriptName
        self.revisionNumber = revisionNumber
        self.scriptDuration = scriptDuration
    
    def print(self):
        print(f"testId: {self.testId}")
        print(f"scriptName: {self.scriptName}")
        print(f"revisionNumber: {self.revisionNumber}")
        print(f"scriptDuration: {self.scriptDuration}\n")

        
def main():
    q = quickViewer()
    q.dumpDetails()

if __name__ == '__main__':
    main()

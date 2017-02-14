import sys, requests as r
#This script takes 4 arguments to add a list of github usernames
#and adds them as collaborators to a repository of your choice.
#The format for the command is python gitCollab.py <username> <repo_name> <pathTo_file> <password>"


try:
    username = sys.argv[1]
    repo = sys.argv[2]
    fname = sys.argv[3]
    addToRepo(username, repo, fname, sys.argv[4])
except IndexError:
    print "Not enough arguments provided"

def addToRepo(username, repo, filename, password):
    if len(sys.argv) == 1:
        print "Format is: python gitcollab.py <username> <repo_name> <pathTo_file> <password>"
        return

    if len(sys.argv) < 5:
        print "Not enough arguments"
        return
        pass


    with open(fname) as f:
        content = f.readlines()
        pass
    content = [x.strip() for x in content]

    url = "https://api.github.com/repos/"

    for name in content:
        print name
        response = r.put(url+username+"/"+repo+"/collaborators/"+name, auth=(sys.argv[1],sys.argv[4]))
        print response



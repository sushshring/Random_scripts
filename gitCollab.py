import sys, requests as r, getpass
#This script takes 4 arguments to add a list of github usernames
#and adds them as collaborators to a repository of your choice.
#The format for the command is python gitCollab.py <username> <repo_name> <pathTo_file> <password>"



def addToRepo(username, repo, filename):

    if len(sys.argv) < 4:
        print "Not enough arguments"
        print "Format is: python gitcollab.py <username> <repo_name> <pathTo_file> <password>"
        return
        return
        pass


    with open(fname) as f:
        content = f.readlines()
        pass
    content = [x.strip() for x in content]

    url = "https://api.github.com/repos/"
    
    password = getpass.getpass("Enter password for github user " + username)

    for name in content:
        print name
        response = r.put(url+username+"/"+repo+"/collaborators/"+name, auth=(sys.argv[1],password))
        print response

try:
    username = sys.argv[1]
    repo = sys.argv[2]
    fname = sys.argv[3]
    addToRepo(username, repo, fname)
except IndexError:
    print "Not enough arguments provided"
    print """Requires four arguments:
            1) github username <username>
            2) github repository <repo>
            3) text file with usernames to add as collaborators, separated by line."""


#!/usr/bin/python
import sys, requests, getpass, argparse

parser = argparse.ArgumentParser(description="This script will initialize a new repository on Github.")
parser.add_argument("-u", '--username', metavar='<Username>', type=str, help='Input your username for github here')
parser.add_argument("-d", '--description', metavar='<description>', type=str, help='The description for the new repository')
parser.add_argument("-n", '--name', metavar='<name>', type=str, help='The name for the new repository')



args = parser.parse_args()


headers = {
    'Content-Type': 'application/json',
}

data = '{"name": "'+args.name+ '", "description":"'+args.description+'","public" :"true", "has_issues":"true", "has_wiki":"false"}'

password = getpass.getpass("Enter password for GitHub username: " + args.username)
r = requests.post('https://api.github.com/user/repos', headers=headers, data=data, auth=(args.username, password))

print r.json()  

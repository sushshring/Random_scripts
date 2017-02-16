import sys, requests

args = sys.argv

if len(args) < 5:
    sys.exit("Arguments invalid")

headers = {
    'Content-Type': 'application/json',
}

data = '{"name": "'+args[1]+ '", "description":"'+args[2]+'","public" :"true", "has_issues":"true", "has_wiki":"false"}'

r = requests.post('https://api.github.com/user/repos', headers=headers, data=data, auth=(args[3], args[4]))

print r.json()  

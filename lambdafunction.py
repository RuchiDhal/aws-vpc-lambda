import json
import requests

def handler(event, context):
    d = ""
    try:
        github_repo = 'https://api.github.com/repos/ruchidhal/ruchidhal/readme'
        response = requests.get(github_repo)
        data = response.json()
        
        readme_content = data['content']
        decoded_content = base64.b64decode(readme_content).decode('utf-8')
        print("README Content:", decoded_content)
        
        d = 'Success'
    except:
        d = 'Fail'
        print("Error fetching README content from GitHub repository")
    
    return d

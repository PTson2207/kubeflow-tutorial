import sys
sys.path.insert(0, "..")
from constants import USERNAME, PASSWORD, NAMESPACE, HOST
import requests

def get_session_cookie():
    session = requests.Session()
    response = session.get(HOST)
    
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {"login": USERNAME, "password": PASSWORD}
    session.post(response.url, headers=header, data=data)
    session_cookie = session.cookies.get_dict()["authservice_session"]
    
    return session_cookie
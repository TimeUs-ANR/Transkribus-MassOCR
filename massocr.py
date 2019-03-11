# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup

# ------------------------------------
username = ""
password = ""
collection = ""
#ex : collection = "7392"
documents = []
# ex : documents = [0001, 45754, 35364] etc.

# -------------------------------------
def authentificate():
    url = "https://transkribus.eu/TrpServer/rest/auth/login"
    payload = 'user=' + username + '&' + 'pw=' + password
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        soup = BeautifulSoup(response.text, "xml")
        session_id = soup.sessionId.string
        print("User successfully authentified.")
    except Exception as e:
        print("Authentification failed:")
        print(e)
        session_id = ''
    return session_id


def getpages(session_id, documents):
 	url = "https://transkribus.eu/TrpServer/rest/collections/%s/%s/fulldoc" % (collection, document)
 	querystring = {"JSESSIONID":session_id}
 	response = requests.request("GET", url, params=querystring)
 	json_file = json.loads(response.text)
 	pages = json_file["md"]["nrOfPages"]
 	print(document)
 	print(pages)
 	return pages


def startocr(session_id, document, pages):
	url = "https://transkribus.eu/TrpServer/rest/recognition/ocr?collId=%s&id=%s&pages=%s&language=French&typeFace=combined" % (collection, document, pages)
	querystring = {"JSESSIONID":session_id}
	response = requests.request("POST", url, params=querystring)
	stat = response.status_code
	print(stat)
	return


# ----

session_id = authentificate()
if session_id:
	for document in documents:
		pages = getpages(session_id, document)
		pages = "1-%s" % pages
		print(pages)
		startocr(session_id, document, pages)

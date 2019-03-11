# Transkribus-MassOCR
Simple scripts to start jobs on Transkribus through the REST API.

## `massocr.py` 
Will send requests to start OCR jobs on Transkribus when provided with user's credits, collection's ID and a list of documents ID from the collection. 

By default, we set language to French and typeface to Combined. 

> More details : https://transkribus.eu/wiki/index.php/REST_Interface#Jobs

### Requirements
- requests>=2.20.0
- lxml>=4.2.1
- beautifulsoup4

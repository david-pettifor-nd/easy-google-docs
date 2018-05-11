# Easy-Google-Docs

This Python wrapper for the Google API Python package adds a vast amount of functionality for common tasks involving 
Google Docs and Google Sheets.

## Installation

You can install with pip:

``pip install easy-google-docs``

Or download the code and run:

``python setup.py install``

## Account Setup

It is important to first setup how you plan on accessing your data.  This falls under one of two different account types:
* Web-based authentication (authenticates as _your_ account)
* Service-account authentication (allows for non-interfacing scripting)

#### Web-Based Authentication:

##### Pros:
* Everything you do will be done as *you* - no need to mess with permissions, etc.
* All files you upload will be to *your* drive space.
* More secure as you must authenticate as yourself every time the script runs

##### Cons:
* Requires human-interface for authentication every time you authenticate
* Cannot automate script/run on GUI-less server

#### Service-Account Authentication:

##### Pros:
* *Can* automate scripts/requires no interfacing
* Gets its own drive space (also a *con*)

##### Cons:
* Gets its own drive space - this means all files uploaded are to *this* account and not *yours*.  You then must
share the file with yourself.
* All files existing in *your* drive space you want to work with must be shared with the service account before it
can *see* them.


#### Steps to Get Started:

##### Create A Project
1. Go to your Google Console to create a new project: [https://console.cloud.google.com/projectcreate]
2. Give your project a name ('Example Project') and click "Create"
3. You will be taken to the main dashboard [https://console.cloud.google.com/home/dashboard].

##### Enable APIs
1. Go to the "Google Drive API" dashboard: [https://console.cloud.google.com/apis/library/drive.googleapis.com] Make
sure your project ('Example Project') is selected in the drop-down menu at the top.
2. Click "Enable"
3. Go to the "Google Sheets API" dashboard: [https://console.cloud.google.com/apis/library/sheets.googleapis.com] Make
sure your project ('Example Project') is selected in the drop-down menu at the top.
4. Click "Enable"

##### Create Credentials

Seriously consider what kind of authentication method you would like to use.  This will heavily depend on your project's
needs, and may mean more or less work in your code.

1. Go to [https://console.cloud.google.com/apis/credentials] to start creating credentials.
* If you want to create a web-based authentication credential, select "OAuth client ID".
* If you want to create a service-account credential, select "Service account key"

###### OAuth Client (Web-based Authentication)

1. If this is your first OAuth client for this project, you must configure the consent screen here: 
[https://console.cloud.google.com/apis/credentials/consent?createClient]
2. Fill out the "Product name shown to users" field and click "Save".
3. This should take you back to the OAuth Client screen: [https://console.cloud.google.com/apis/credentials/oauthclient]
4. Select "Other" and give it a name (example: "My Script") and click "Create"
5. Close the pop-up window that shows your "Client ID" and "Secret"
6. On the far-right side of your new credential, click on the Download link to download your client credentails JSON 
file.
7. Keep this JSON file someplace secret!  It will be needed to use this API.

###### Service-Account
1. On the "Create Service Account" page [https://console.cloud.google.com/apis/credentials/serviceaccountkey], 
select "New Service Account" under "Service Account".
2. Give your service account a name ('myserviceaccount').
3. Under "Role", select "Service Accounts" -> "Service Account Admin"
4. Leave the "Key type" as "JSON" and click "Create"
5. Save the returned credentials JSON file someplace safe!  It will be needed to use this API.


## Usage

First import what you need:

```python
from easygoogledocs import GoogleAPI
```

#### Authenticating

Be sure to have your downloaded JSON file ready from the steps above!

```python
# Based on your authentication type, import one or the other
from easygoogledocs import [AUTH_TYPE_BROWSER|AUTH_TYPE_SERVICE_ACCOUNT]

api = GoogleAPI(credentials_file='credentials.json')
api.authorize(authentication_type=[AUTH_TYPE_BROWSER|AUTH_TYPE_SERVICE_ACCOUNT])
```

# DHIS2 DataStore Json loader
A python 3 JSON LOADER for DHIS2 for creation of DHIS2 dataStores. <br>
These scripts uses basic authentication to log into DHIS2 via its web api and load json payloads
to the data store. The script loads the json payload from 'myfolders' directory and each file name becomes a <b>key</b> while the content
becomes the <b>value</b>.<br>
For authentication, a sample 'secrets.json' file with authentication details for multiple dhis2 instances
shown below can be used. One has to select which DHIS2 instance they want to payload uploaded to by setting the <b>selected_secrets</b>
parameter value which begin from zero (0).

{
  "credentials" : [
    {
      "username": "admin",
      "password": "district",
      "baseUrl" : "http://localhost:8181/dhis/api/dataStore/mydatastore1/"
    },
    {
      "username": "admin",
      "password": "district",
      "baseUrl" : "https://mydomain/dss/api/dataStore/mydatastore2/"
    }
  ]
}
## Password Generator
Also contained in this repo is a password generator script (PasswordGenerator.py) that can be used to generate DHIS2 salted
passwords. Once the password has been created, use sql update query to update a particular users password.

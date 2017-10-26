# json_loader
A python 3 JSON LOADER for DHIS2. These scripts use basic authentication to log into DHIS2 via its web api and load json payloads 
to the data store. For authentication, a sample 'secrets.json' file with authentication details for multiple dhis2 instances 
shown below can be used.

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

Also contained in this repo is a password generator script (PasswordGenerator.py) that can be used to generate DHIS2 salted
passwords. Once the password has been created, use sql update query to update a particular users password.

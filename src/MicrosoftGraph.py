#!/usr/bin/env python3

import json
import requests

class AzureActiveDirectory(object):
    def __init__(self, aad_id, resource):
        self.AzureActiveDirectoryID = aad_id
        self.Resource = resource
    
    def PostAuthenticationEndpoint(self, client_id, client_secret, grant_type): #client_id, client_secret
        """
            Sends a POST request to Azure Active Directory Authentication's 
            endpoint to receive an access token for this application in response.

            Args:
                aad_id          : Azure Active Directory ID or Name
                client_id       : The client ID of the application
                client_secret   : The client secret of the application
                resource        : The name of the resource that needs to be accessed
                grant_type      : The name of the grant flow scenario type

            Returns:
                AAD Token as JSON response.
        """        
        aad_auth_endpoint = "https://login.microsoftonline.com/{}/oauth2/token".format(self.AzureActiveDirectoryID)
        app_credentials = {
            "client_id" : client_id,
            "client_secret" : client_secret,
            "resource" : self.Resource,
            "grant_type" : grant_type
        }

        return json.loads(requests.post(aad_auth_endpoint, data = app_credentials).text)

    def GetToken(self, response):
        """
            Args:
                response : The Client Credentials Grant Flow result as JSON response
            Returns:
                The Access Token required for the previously defined resource 
                type as a base64 string.
        """
        return response['access_token']

class OneDrive(AzureActiveDirectory):
    def __init__(self, aad_id):
        self.Resource = "https://graph.microsoft.com"
        super().__init__(aad_id, self.Resource)

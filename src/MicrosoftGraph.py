#!/usr/bin/env python3

import json
import requests
from requests_oauthlib import OAuth2Session

class AzureActiveDirectory(object):
    @staticmethod
    def get_token(aad_id, client_id, client_secret, resource, grant_type): #client_id, client_secret
        """
            Send a POST request to Azure Active Directory Authentication's 
            endpoint to receive an access token for this application.

            Args:
                aad_id          : Azure Active Directory ID or Name
                client_id       : The client ID of the application
                client_secret   : The client secret of the application
                resource        : The name of the resource that needs to be accessed
                grant_type      : The name of the grant flow scenario type

            Returns:
                AAD Token as JSON response.
        """        
        aad_auth_endpoint = "https://login.microsoftonline.com/{}/oauth2/token".format(aad_id)
        app_credentials = {
            "client_id" : client_id,
            "client_secret" : client_secret,
            "resource" : resource,
            "grant_type" : grant_type
        }

        return json.loads(requests.post(aad_auth_endpoint, data = app_credentials).text)

class OneDrive(AzureActiveDirectory):
    # https://graph.microsoft.com/v1.0/me/drive/root:/画像/アニメ:/children
    pass

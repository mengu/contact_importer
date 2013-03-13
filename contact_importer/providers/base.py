
class BaseProvider(object):

    def __init__(self, client_id, client_secret, redirect_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url

    def request_authorization(self, redirect_url):
        raise NotImplementedError("Not implemented")

    def request_access_token(self, code, redirect_url):
        raise NotImplementedError("Not implemented")

    def import_contacts(self, access_token):
        raise NotImplementedError("Not implemented")

    def parse_contacts(self, access_token):
        raise NotImplementedError("Not implemented")
    

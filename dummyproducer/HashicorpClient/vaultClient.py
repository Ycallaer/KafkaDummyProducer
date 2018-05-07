import hvac

class VaultClient():
    def __init__(self):
        self.client = hvac.Client(url='http://localhost:8200')
        self.client.auth_userpass("vault_user", "vault_pass")

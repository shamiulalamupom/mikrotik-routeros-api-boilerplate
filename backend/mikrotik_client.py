from routeros_api import RouterOsApiPool
from config import MikrotikConfig

class MikroTikClient:
    def __init__(self):
        self.pool = RouterOsApiPool(
            MikrotikConfig.HOST,
            username=MikrotikConfig.USERNAME,
            password=MikrotikConfig.PASSWORD,
            port=MikrotikConfig.PORT,
            use_ssl=MikrotikConfig.USE_SSL,
            plaintext_login=MikrotikConfig.PLAIN_TEXT_LOGIN,
        )
        self.api = self.pool.get_api()

    def get_interfaces(self):
        return list(self.api.get_resource('/interface').get())

    def get_ip_addresses(self):
        return list(self.api.get_resource('/ip/address').get())

    def add_ip_address(self, address, interface):
        ip_res = self.api.get_resource('/ip/address')
        ip_res.add(address=address, interface=interface)

    def close(self):
        self.pool.disconnect()

from BeautifulSoup import BeautifulSoup
from requests import get


class Backend(object):
    url = 'http://%s/status/arp.html'

    def __init__(self, host, username, password):
        self.url = self.url % host
        self.credentials = (username, password)

    def main(self, mac):
        r = get(self.url, auth=self.credentials)
        host_rows = BeautifulSoup(r.text).body.form('tr')[2:]

        print [host.td.text for host in host_rows if mac in host.text][0]


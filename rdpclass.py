import listprops


class Doc(listprops.ListProps):
	"""Connect to a terminal server with default options, which can be overridden, and a host (or ip-address) as required parameter.
	    The default options are to connect as a domain administrator in a full-screen window.
	    Changeable options are program parameters, username and window geometry.

	    Example:
		r = Rdp('hostname')
		r.launch()

	    Change default options:
		r.user = 'guestuser [-d domain]'
		r.geometry = '-g 800x600'
		r.parms = '-n -a 16'

	"""

class Rdp(listprops.ListProps):

    def __init__(self, host):
        self.host = host
        self.parms = '-D -n -a 16'
        self.user = 'administrator -d domein'
        self.geometry = '-f'


    def launch(self):
        self.constring = '/usr/bin/rdesktop {} -u {} {} {}'.format(self.parms, self.user, self.geometry, self.host)
        print (self.constring)




if __name__ == '__main__':
    r = Rdp('rdp')
    print (r)

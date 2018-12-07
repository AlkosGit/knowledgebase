# file: knowledgebase/apache.py
from listprops import ListProps

class Doc(ListProps):
    """
    Install and configure Apache webserver to serve content created with Django.


    Installation (Fedora):
        # dnf install httpd python3-mod_wsgi

    Configuration:
    Create conf file for Django:
        #/etc/httpd/conf.d/django.conf

    Alias /static /opt/printermanagement/printer/static
    <Directory /opt/printermanagement/printer/static>
     Require all granted
    </Directory>

    <Directory /opt/printermanagement/printmgmt>
        <Files wsgi.py>
         Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess printermanagement python-path=/opt/printermanagement:/opt/printermanagement/lib/python3.7/site-packages
    WSGIProcessGroup printermanagement
    WSGIScriptAlias / /opt/printermanagement/printmgmt/wsgi.py

    """

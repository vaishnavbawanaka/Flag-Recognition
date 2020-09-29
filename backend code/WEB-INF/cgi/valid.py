import cgi
import datetime
import os
from http.cookies import *

#form=cgi.FieldStorage()
print("Content-type: text/html\n\n")

html='''
<html>
<body>
<div id="content">
       
      </div>

</body>
</html>


'''


print(html.format(**locals()))
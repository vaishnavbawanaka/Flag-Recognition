import cgi
import datetime
import os
from http.cookies import *

#form=cgi.FieldStorage()
print("Content-type: text/html\n\n")

html='''<html>
<head>
	<title>Bottom page</title>
</head>
<body>
	<table border="0" width="100%">
		<tr>
			<td valign="bottom" style="font-size:20px;color:black;font-face=Arial">Developed by Vaishnav, Sreekar,Priyanka & Shubham</td>
		</tr>
	</table>
</body>
</html>
'''

print(html.format(**locals()))

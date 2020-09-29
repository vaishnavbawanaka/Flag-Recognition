import cgi
import datetime
import os
from http.cookies import *

#form=cgi.FieldStorage()
print("Content-type: text/html\n\n")

html='''<html>
 
  <body bgcolor="#FFFAF0">
      <table border="0" width="100%">
        <tr width="100%">
        <td align="center" width="10%" style="font-size:20px;color:violet"><a id="a1" href="home.py" style="text-decoration:none" target="f1">HOME</a></td>
        <td align="center" width="10%" style="font-size:20px;color:violet"><a id="a1" href="animals.py" style="text-decoration:none" target="f1">COUNTRIES</a></td>
        <td align="center" width="10%" style="font-size:20px;color:violet"><a id="a2" href="cnn.py" style="text-decoration:none" target="f1">CNN</a></td>
        <td align="center" width="20%" style="font-size:20px;color:violet"><a id="a3" href="valid.py" style="text-decoration:none" target="f1">TRAINING AND VALIDATION</a></td>
        <td align="center" width="20%" style="font-size:20px;color:violet"><a id="a1" href="contact.py" style="text-decoration:none" target="f1">ABOUT US</a></td>
        </tr>
      </table>
  </body>
</html>

'''

print(html.format(**locals()))

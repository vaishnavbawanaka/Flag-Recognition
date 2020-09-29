import cgi
import datetime
import os
from http.cookies import *
import sys
print("Content-type: text/html\n\n")
import ClassificationProject.modelling.CNN32x32.model as model

form=cgi.FieldStorage()


html='''
<html>
<body align="center" bgcolor="#FFFAF0">
<form enctype="multipart/form-data" method=POST>
<table align="center" border=0>
<tr>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <td >&emsp;<b>Upload Photo </b>&emsp;
        <input type="file" name="file_img"></td>
        
        <td align="center"><input type="submit" name="sub1" value="Predict"></td>
</tr>

</table>
</form>
</body>
</html>

'''

if "sub1" in form:#to save changes in new details form
    fileitem = form['file_img']
        # Test if the file was uploaded
    #print(fileitem)
    if fileitem.filename:
        # strip leading path from file name to avoid directory traversal attacks        
        fn = os.path.basename(fileitem.filename)
        open('../../' + fn, 'wb').write(fileitem.file.read())
        message = 'The file "' + fn + '" was uploaded successfully'
        try:
            prd=model.model_run(fn)
            lst=prd.split("\\")
            prd=lst[len(lst)-1]
            html='''
            <html>
            	<body>
            <br></br>
            <br></br>
    
            	<table align="center" width="100%">   
            	<tr align="center" width="100%">            
            		<center><img src="../'''+str(fn)+'''"/></center>
            	</tr>
              <!-- <tr align="center">Predicted Country = '''+prd+'''</tr>-->        		
            	</table>            
            <p ALIGN=CENTER>Predicted Country = '''+prd+'''</p>
            	</body>
            </html>
            '''
            
        except Exception as ex:
            html='''<html><body>Exception'''+ex+'''</body></html>'''
        
        

    else:
        message = 'No file was uploaded'
    #print(message)


print(html.format(**locals()))


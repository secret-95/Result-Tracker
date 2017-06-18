import os
import re
import smtplib
import urllib2
import gtk.gdk
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
#Extract the contents of the website
html_content=urllib2.urlopen('http://www.sjce.ac.in/results').read()
#finds if the results have been announced 
matches=re.findall('results have been announced',html_content)
if len(matches)==0:
	print 'not found'
else:
	w = gtk.gdk.get_default_root_window()
	sz = w.get_size()
	print "The size of the window is %d x %d" % sz
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	if (pb != None):
	    pb.save("/home/secret95/Desktop/Tracker/screenshot.png","png")
	else:
 	   print "Unable to get the screenshot."

	img_data = open("/home/secret95/Desktop/Tracker/screenshot.png", 'rb').read()
	msg = MIMEMultipart()
	msg['Subject'] = 'subject'
	msg['From'] = 'test@gmail.com'
	msg['To'] = 'test@gmail.com'
	text = MIMEText("test")
	msg.attach(text)
	image = MIMEImage(img_data, name=os.path.basename("/home/secret95/Desktop/Tracker/screenshot.png"))
	msg.attach(image)
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login("test@gmail.com","testpassword") 
	s.sendmail("test@gmail.com","test@gmail.com",msg.as_string())
	s.quit()
	print 'Email sent'
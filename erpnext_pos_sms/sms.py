from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, getdate, today
from frappe import throw, _
from frappe.utils.nestedset import NestedSet, get_ancestors_of, get_descendants_of
import json 
import time
import urllib
from urllib.request import urlretrieve



def send_sms(doc, event):
    mobile_number = frappe.db.get_value('Customer', {'name': doc.customer}, ['mobile_no'])
    from frappe.core.doctype.sms_settings.sms_settings import send_sms
    #url = "http://store1.frapino.in/files/{}.pdf".format(doc.name)
    sales =doc.doctype
    sales = sales.replace(" ","+")

    #url = "http://" + frappe.request.host + "/api/method/frappe.utils.print_format.download_pdf?doctype="+sales +"&name={}".format(doc.name)+"&format=Natural"+"&no_letterhead=0"
    #url = "http://store1.frapino.in/files/{}.pdf".format(doc.name)
    
    #message = "Thank you for your purchase at Frapino. You have spent Rs " + str(doc.grand_total) + " via Cash on : "  + (doc.posting_date) + "."+" " + "Click the link to view your invoice" + " "+ url
    message = "Thank you for your purchase at Frapino. You have spent Rs " + str(doc.grand_total) + " via Cash on : "  + (doc.posting_date).
    send_sms([mobile_number], msg=message)

    
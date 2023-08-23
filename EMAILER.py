# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:34:11 2023

@author: monke
"""

# Import modules
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd
firstName = 'Mohammed'
# Define the HTML document
html = '''
    <h1>Looking for students this summer?</h1>

<p>Dear {first name},</p>

<p>I hope this email finds you well. As you may or may not already know, the UK recently started a Visa waiver program that allows nationals from the countries of&nbsp;Bahrain, Kuwait, Oman, Qatar, Saudi Arabia and the United Arab Emirates to stay in the UK for tourism, studying and business. Off the back of this Saudi airlines and Emirates airlines are both increasing their flights to the UK and here at Gulf conferences we&#39;re anticipating a lot of residents from these countries to take advantage of this scheme to study here this summer.</p>

<p>https://www.gov.uk/get-electronic-visa-waiver#:~:text=An%20EVW%20lets%20you%20visit,48%20hours%20before%20you%20travel.</p>

<p>https://www.emirates.com/media-centre/emirates-expands-its-a380-network-with-the-resumption-of-services-to-birmingham-glasgow-and-nice/#:~:text=With%20the%20return%20of%20the,line%20with%20growing%20travel%20demand.</p>

<p>I&#39;m reaching out to you now to ask about any summer programmes you offer and to book a meeting with you soon so that we can discuss potnetial agency agreements. We have already have strong relationships with the governements of all these countries and now we&#39;re offering our extensive knowledge and network to help you capitalise on the new EVW being offered by the governement. If this is something you are interested in then please reply so we can get things moving ASAP.</p>

<p>Kind regards,</p>

<p>&nbsp;</p>

<div dir="ltr"><div><br></div><div><table cellpadding="0" cellspacing="0" style="color:rgb(255,255,255);font-size:medium;vertical-align:-webkit-baseline-middle;font-family:Arial"><tbody><tr><td style="vertical-align:top"><table cellpadding="0" cellspacing="0" style="vertical-align:-webkit-baseline-middle;font-family:Arial"><tbody><tr><td style="text-align:center"></td></tr><tr><td height="30"><img src="https://ci5.googleusercontent.com/proxy/NLFtJaFfEBQVLZ-w1teoOvCgb7q_CYR5LlPR70SydPymalgZ4jvR1aq7YF_Mj3iEfhhj3qfBMNvQJK4tjxSKLo3BDtxJMbVVmbinOEZY4ZTdyag=s0-d-e1-ft#https://drive.google.com/uc?id=1AYR083wyALdnJcimvYmLYIHZdOxS2zy-" width="121" height="64" style="display:block;margin-right:0px"></td></tr><tr><td style="text-align:center"><table cellpadding="0" cellspacing="0" style="vertical-align:-webkit-baseline-middle;font-family:Arial;display:inline-block"><tbody><tr><td><a href="https://www.facebook.com/gulfconference/" color="#e19c35" style="color:rgb(17,85,204);display:inline-block;padding:0px;background-color:rgb(225,156,53)" target="_blank"><img src="https://ci6.googleusercontent.com/proxy/CsU8Viqi3BJDAFLrGZPksmkYgWVO33uPMuUPYTdIjlZGkYPTUoI_vJDzFKjQFwApPgNeOzuP2McTvftBr9y45oU4K7hT_3YVrqR7L-3VwYbeIS13VrCdWig_8JnKG5CZ_mBs7omd-uFCFStjfCVo=s0-d-e1-ft#https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/facebook-icon-2x.png" alt="facebook" color="#e19c35" height="24" style="max-width:135px;display:block"></a></td><td width="5"><div></div></td><td><a href="https://twitter.com/gulfeducationco?lang=en" color="#e19c35" style="color:rgb(17,85,204);display:inline-block;padding:0px;background-color:rgb(225,156,53)" target="_blank"><img src="https://ci5.googleusercontent.com/proxy/7hurPF5R2XfTJTr2Fqhp-g90VfcTNaZV-l9jil-wiHwtT5Ml1DQ7jOF4iK6ioEc0wAAWwT4hZgaXYPuOg4zJ5G-cClwKcyCAVyjvb3__WdNvjK_wisecltPdtxx2obIkLOEh82rck1AaTEV-FxA=s0-d-e1-ft#https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/twitter-icon-2x.png" alt="twitter" color="#e19c35" height="24" style="max-width:135px;display:block"></a></td><td width="5"><div></div></td><td><a href="http://linkedin.com/in/nicetoconnect" color="#e19c35" style="color:rgb(17,85,204);display:inline-block;padding:0px;background-color:rgb(225,156,53)" target="_blank"><img src="https://ci6.googleusercontent.com/proxy/8VnMNxHLCZ0mb5p6kFUeerh69ZxNFn796FO-bPB4zCIy6zKpR1zhFWOLua5F0V0VgIit8AVUmjEgifJrk7e9BwF3wOGdMevsrii7gV2oBOFEo5guBdtnCAwg1eRcW3MR-HHxsstpA8fhJPI5apj8=s0-d-e1-ft#https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/linkedin-icon-2x.png" alt="linkedin" color="#e19c35" height="24" style="max-width:135px;display:block"></a></td><td width="5"><div></div></td><td><a href="https://www.instagram.com/gulfconferencesuk/" color="#e19c35" style="color:rgb(17,85,204);display:inline-block;padding:0px;background-color:rgb(225,156,53)" target="_blank"><img src="https://ci4.googleusercontent.com/proxy/N8g6tZ7eglyo7c_6d8oDw66CnB6TXXjsEzJARvc9fD3jikHSnoEtAs2zQjlpsa6zX3aAyD6apMdrUeWhCbbT_8rbyW-AqHOjfQQWIa_UrT_KpQ4kKh1zjDP5nh-osDYyAh4XeiSmeBBT1nFHzi8PtQ=s0-d-e1-ft#https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/instagram-icon-2x.png" alt="instagram" color="#e19c35" height="24" style="max-width:135px;display:block"></a></td><td width="5"><div></div></td></tr></tbody></table></td></tr></tbody></table></td><td width="46"><div></div></td><td style="padding:0px;vertical-align:middle"><h3 color="#000000" style="margin:0px;font-size:18px;color:rgb(0,0,0)">Mohammed Osman</h3><p color="#000000" style="margin:0px;color:rgb(0,0,0);font-size:14px;line-height:22px">Middle East Director</p><p color="#000000" style="margin:0px;color:rgb(0,0,0);font-size:14px;line-height:22px">Gulf Conferences Ltd</p><table cellpadding="0" cellspacing="0" style="vertical-align:-webkit-baseline-middle;font-family:Arial;width:281.6px"><tbody><tr><td height="30"></td></tr><tr><td color="#2676dd" height="1" style="width:281.6px;border-bottom:1px solid rgb(38,118,221);border-left:none;display:block"></td></tr><tr><td height="30"></td></tr></tbody></table><table cellpadding="0" cellspacing="0" style="vertical-align:-webkit-baseline-middle;font-family:Arial"><tbody><tr height="25" style="vertical-align:middle"><td width="30" style="vertical-align:middle"><table cellpadding="0" cellspacing="0" style="vertical-align:-webkit-baseline-middle;font-family:Arial"><tbody><tr><td style="vertical-align:bottom"><span color="#2676dd" width="11" style="display:block;background-color:rgb(38,118,221)"><img src="https://ci6.googleusercontent.com/proxy/Xq3hntJEq2rjJzR0uWCVm3clsSla7NsI7xyRuy0B6esGxKEs0TJKSCBJd0PTJnw80_-gOm3yRwJoGtSWipm4TqjnmSCEllHm6WPq2oze68mmA8DO6Mj2dGBHroByKflVGCBL0c-wyQ3vCF92=s0-d-e1-ft#https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/phone-icon-2x.png" color="#2676dd" width="13" style="display:block"></span></td></tr></tbody></table></td><td style="padding:0px;color:rgb(0,0,0)"><a color="#000000" style="font-size:12px">+44 7440104125</a>&nbsp;</td></tr><tr height="25" style="vertical-align:middle"><td width="30" style="vertical-align:middle"><table cellpadding="0" cellspacing="0" style="vertical-align:-webkit-baseline-middle;font-family:Arial"><tbody><tr><td style="vertical-align:bottom"><span color="#2676dd" width="11" style="display:block;background-color:rgb(38,118,221)"><img src="https://ci5.googleusercontent.com/proxy/u9Dqq8IRTYcA9pxGhij8X1100IBTEBNk6GfgLex2wy5mIUGt4EvtpI__1csTElV-MUMrqJCa2SjWZkRDmYNbTv260GIk6RQb8BWD6Fub4s38olgLolJ-Y0ZMzSkDaCxhCmOgByGso4GxlMz7=s0-d-e1-ft#https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/email-icon-2x.png" color="#2676dd" width="13" style="display:block"></span></td></tr></tbody></table></td><td style="padding:0px"><a href="mailto:mohamed@gulfconferences.co.uk" color="#000000" style="color:rgb(0,0,0);font-size:12px" target="_blank">mohamed@gulfconferences.co.uk</a></td></tr><tr height="25" style="vertical-align:middle"><td width="30" style="vertical-align:middle"><table cellpadding="0" cellspacing="0" style="vertical-align:-webkit-baseline-middle;font-family:Arial"><tbody><tr><td style="vertical-align:bottom"><span color="#2676dd" width="11" style="display:block;background-color:rgb(38,118,221)"><img src="https://ci5.googleusercontent.com/proxy/bDGbdhNSZAZaKWHjXdHMW3DL3PklwLU9F5lSquHVukVuOVNDm_0LSPw8ckOtJwduaqdVOyJnATN5reUqPaX3QjUNCZkwbG2Ac8UdOzrywgI_nREPLk66UFxOhX3uiKMJOqLfWEBJyXQ51Tk=s0-d-e1-ft#https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/link-icon-2x.png" color="#2676dd" width="13" style="display:block"></span></td></tr></tbody></table></td><td style="padding:0px"><a href="https://www.gulfconferences.co.uk/" color="#000000" style="color:rgb(0,0,0);font-size:12px" target="_blank">www.gulfconferences.co.uk</a></td></tr><tr height="25" style="vertical-align:middle"><td width="30" style="vertical-align:middle"><table cellpadding="0" cellspacing="0" style="vertical-align:-webkit-baseline-middle;font-family:Arial"><tbody><tr><td style="vertical-align:bottom"><span color="#2676dd" width="11" style="display:block;background-color:rgb(38,118,221)"><img src="https://ci5.googleusercontent.com/proxy/PMsX6QYblfid2-Aq_atF0w8D-5O2KEMGfclrImAJEOsQqE_sbKhMfAd7gH3akRnGu3ErEwVfaOuRfuDxpUBCSL-LKhPfwPnP1FnJHgaOjcrmV2CgMlczkQKYJb-bo0qnAEo7PcQNq51IElkIZFk=s0-d-e1-ft#https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/address-icon-2x.png" color="#2676dd" width="13" style="display:block"></span></td></tr></tbody></table></td><td style="padding:0px"><span color="#000000" style="font-size:12px;color:rgb(0,0,0)">14 Alexandria Road, Ealing, London, W13 0NR<br></span></td></tr></tbody></table></td></tr></tbody></table></div></div>
    '''

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'mohamed@gulfconferences.co.uk'
password = 'M123456789'
email_to = 'mohamed@gulfconferences.co.uk'


# Generate today's date to be included in the email Subject
date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = 'Summer Study Oppurtunities'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))
# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, password)
    server.sendmail(email_from, email_to, email_string)
from statik.templatetags import register

def escape_email(email_str):
	return email_str.replace('@', ' [at] ').replace('.', ' [dot] ')

@register.filter(name="emailify")
def emailify(email_str): #alxegod@gmail.com -> <a href="mailto:alxegod@gmail.com">alxegod [at] gmail [dot] com</a>
	return "<a href=\"mailto:{0!s}\">{1!s}</a>".format(email_str, escape_email(email_str))

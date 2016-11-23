from statik.templatetags import register

@register.filter(name="urlify")
def urlify(path):
	if path is None:
		return None

	return "<a href=\"{0!s}\">{0!s}</a>".format(path)

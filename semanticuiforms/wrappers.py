# Wrappers
FIELD_WRAPPER = (
	"<div class=\"%(class)sfield\">%(label)s%(field)s%(errors)s</div>"
)

ERROR_WRAPPER = (
	"<div class=\"ui red pointing prompt label\">%(message)s</div>"
)

INPUT_WRAPPER = (
	"<div class=\"ui%(style)sinput\">%(icon)s%(field)s</div>"
)

CHECKBOX_WRAPPER = (
	"<div class=\"ui%(style)scheckbox\">%(field)s%(label)s</div>"
)

DROPDOWN_WRAPPER = (
	"<div class=\"ui%(style)sselection dropdown\">"
		"<input name=\"%(name)s\"%(attrs)stype=\"hidden\">"
		"<i class=\"dropdown icon\"></i>"
		"<div class=\"default text\">%(placeholder)s</div>"
		"<div class=\"menu\">"
			"%(choices)s"
		"</div>"
	"</div>"
)

CALENDAR_WRAPPER = (
	"<div class=\"ui%(style)scalendar\">"
		"<div class=\"ui input%(align)sicon\">"
			"%(icon)s%(field)s"
		"</div>"
	"</div>"
)


# Templates
LABEL_TEMPLATE = (
	"<label for=\"id_{}\">{}</label>"
)

ICON_TEMPLATE = (
	"<i class=\"{} icon\"></i>"
)

CHOICE_TEMPLATE = (
	"<div class=\"item\" data-value=\"{}\">{}</div>"
)

ICON_CHOICE_TEMPLATE = (
	"<div class=\"item\" data-value=\"{}\">{}{}</div>"
)

COUNTRY_TEMPLATE = (
	"<div class=\"item\" data-value=\"{}\">"
	"<i class=\"{} flag\"></i> {}"
	"</div>"
)
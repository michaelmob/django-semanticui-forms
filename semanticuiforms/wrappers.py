from django.conf import settings


# Wrappers
FIELD_WRAPPER = getattr(settings, "SUI_FIELD_WRAPPER", (
	"<div class=\"%(class)sfield\">"
		"%(label)s"
		"%(field)s"
		"%(errors)s"
		"%(help)s"
	"</div>"
))

ERROR_WRAPPER = getattr(settings, "SUI_ERROR_WRAPPER", (
	"<div class=\"ui red pointing prompt label\">%(message)s</div>"
))

INPUT_WRAPPER = getattr(settings, "SUI_INPUT_WRAPPER", (
	"<div class=\"ui%(style)sinput\">%(icon)s%(field)s</div>"
))

CHECKBOX_WRAPPER = getattr(settings, "SUI_CHECKBOX_WRAPPER", (
	"<div class=\"ui%(style)scheckbox\">%(field)s%(label)s</div>"
))

DROPDOWN_WRAPPER = getattr(settings, "SUI_DROPDOWN_WRAPPER", (
	"<div class=\"ui%(style)sselection dropdown\">"
		"<input name=\"%(name)s\"%(attrs)stype=\"hidden\"></input>"
		"%(icon)s"
		"<div class=\"default text\">%(placeholder)s</div>"
		"<div class=\"menu\">"
			"%(choices)s"
		"</div>"
	"</div>"
))

MULTIPLE_DROPDOWN_WRAPPER = getattr(settings, "SUI_MULTIPLE_DROPDOWN_WRAPPER", (
	"<div class=\"ui%(style)smultiple selection dropdown\">"
		"%(field)s"
		"%(icon)s"
		"<div class=\"default text\">%(placeholder)s</div>"
		"<div class=\"menu\">"
			"%(choices)s"
		"</div>"
	"</div>"
))

CALENDAR_WRAPPER = getattr(settings, "SUI_CALENDAR_WRAPPER", (
	"<div class=\"ui%(style)scalendar\">"
		"<div class=\"ui input%(align)sicon\">"
			"%(icon)s%(field)s"
		"</div>"
	"</div>"
))

FILE_WRAPPER = getattr(settings, "SUI_FILE_WRAPPER", (
	"%(field)s"
	"<label for=\"%(id)s\" class=\"ui%(style)sbutton\">"
		"%(icon)s<span>%(text)s</span>"
	"</label>"
))


# Templates
LABEL_TEMPLATE = getattr(settings, "SUI_LABEL_TEMPLATE", (
	"<label for=\"id_{}\">{}</label>"
))

ICON_TEMPLATE = getattr(settings, "SUI_ICON_TEMPLATE", (
	"<i class=\"{} icon\"></i>"
))

FLAG_TEMPLATE = getattr(settings, "SUI_FLAG_TEMPLATE", (
	"<i class=\"{} flag\"></i>"
))

CHOICE_TEMPLATE = getattr(settings, "SUI_CHOICE_TEMPLATE", (
	"<div class=\"item\" data-value=\"{}\">{}</div>"
))

ICON_CHOICE_TEMPLATE = getattr(settings, "SUI_ICON_CHOICE_TEMPLATE", (
	"<div class=\"item\" data-value=\"{}\">{}{}</div>"
))

COUNTRY_TEMPLATE = getattr(settings, "SUI_COUNTRY_TEMPLATE", (
	"<div class=\"item\" data-value=\"{}\">"
		"%s {}"
	"</div>"
) % FLAG_TEMPLATE)

HELP_TEMPLATE = getattr(settings, "SUI_HELP_TEMPLATE", (
	"<div class=\"%s\">{}</div>"
) % getattr(settings, "SUI_HELP_CLASS", "ui help"))
FIELD_WRAPPER = """
<div class="%(class)sfield">%(label)s%(field)s%(errors)s</div>
"""[1:-1]

ERROR_WRAPPER = """
<div class="ui red pointing prompt label">%(message)s</div>
"""[1:-1]

INPUT_WRAPPER = """
<div class="ui%(style)sinput">%(icon)s%(field)s</div>
"""[1:-1]

CHECKBOX_WRAPPER = """
<div class="ui%(style)scheckbox">%(field)s%(label)s</div>
"""[1:-1]

DROPDOWN_WRAPPER = """
<div class="ui%(style)sselection dropdown">
	<input name="%(name)s"%(attrs)stype="hidden">
	<i class="dropdown icon"></i>
	<div class="default text">%(placeholder)s</div>
	<div class="menu">
		%(choices)s
	</div>
</div>
"""[1:-1]

CALENDAR_WRAPPER = """
<div class="ui%(style)scalendar">
	<div class="ui input%(align)sicon">
		%(icon)s%(field)s
	</div>
</div>
"""[1:-1]

LABEL_TEMPLATE = """<label for="id_{}">{}</label>"""

ICON_TEMPLATE = """<i class="{} icon"></i>"""

CHOICE_TEMPLATE = """<div class="item" data-value="{}">{}</div>"""

ICON_CHOICE_TEMPLATE = """<div class="item" data-value="{}">{}{}</div>"""

COUNTRY_TEMPLATE = """
<div class="item" data-value="{}">
	<i class="{} flag"></i> {}
</div>
"""[1:-1]
# Semantic UI for Django Forms
Effortlessly style all of your Django forms and form fields with Semantic UI wrappers.


#### Starting Off
1. Install SemanticUIForms
2. Load the templatetags into your template `{% load semanticui %}`

#### Template Tag
To render a form, it's as simple as `{% render_form my_form %}`  
It is also possible to render each field individually allowing for more
customization within the template. `{% render_field my_form.field %}`

#### Custom Attributes
Any attribute can be assigned to most fields. This can be done by either
assigning within the form class or on-the-fly in the template.

**In form class**
```python
field = forms.CharField(widget=forms.TextInput(attrs={"value": "Testing"}))
```

**In template tag**
```html
{% render_field my_form.field value='My Value' placeholder='Put your text here!' %}
```

#### Private Attributes
Specific attributes can modify how your fields are rendered. Private attributes
start with a `_` and will not be added to the field's attributes. These private
attributes can be set in the form class or as an argument like above.

* `_no_label`: Do not show label
* `_no_required`: Do not show required asterisk
* `_no_errors`: Do not show inline errors
* `_override`: Render as a different field type
* `_style`: Stylize specific fields (BoleanField, ChoiceField)
    * `BooleanField`: set to 'toggle' or 'slider'
    * `ChoiceField`: set to 'search' or 'multiple' and more
* `_icon`: Put icon on field
* `_align`: Used with `_icon`, which side icon is on; not required

#### Icons
Icons can be added to input fields easily. Add the private attribute `_icon` and
optionally `_align` to your arguments.

```html
{% render_field my_form.field _icon='star' _align='left' %}
```

#### Override to render as different field
Overriding the function that renders the field is done using the `_override`
private attribute. This is useful for things like using `CountryField` as it is
not its own field type.


#### Special ChoiceFields

**CountryField**  
`CountryField` from the `django-countries` package can be used to create a nice
field that displays a list of countries alongside their flags, to access it you
must set the `_override` private attribute to `CountryField`.

**Icon ChoiceField**  
`IconChoiceField` can be used with overriding just like `CountryField`. This
field is useful since icons can be placed next to the values in the field.

```python
# Python
# ("key", "value|icon")
choices = (
	("male", "Male|man"),
	("female", "Female|woman"),
	("other", "Other|genderless"),
)

# Template
{% render_field my_form.gender _override='IconChoiceField' %}
```
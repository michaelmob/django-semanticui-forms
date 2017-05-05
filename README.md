# Semantic UI for Django Forms
Effortlessly style all of your Django forms and form fields with Semantic UI wrappers.


#### Starting Off
1. Install this `django-semanticui-forms` with pip or git.  
```
pip install django-semanticui-forms
```
2. Add `semanticuiforms` to your `INSTALLED_APPS`.
3. Load the templatetags into your template `{% load semanticui %}`  

#### Template Tag
To render a form, it's as simple as `{% render_form my_form %}`  

It is possible to render each field individually allowing for more
customization within the template. `{% render_field my_form.field %}`  

## Attributes
#### Form Attributes  
Form attributes given to the template tag that are not specified for internal
use are passed onto each field.

It is possible to exclude fields from `render_form` using the `exclude` parameter.
Fields to be excluded should be separated by commas.  
```html
{% render_form my_form exclude='field1,field3' %}
```  

For example: `{% render_form my_form name='Hello' %}` will add a name attribute
to each field in that form.

For good use: `{% render_form my_form _help=1 %}` will display the field's
help_text on all fields.  

 #### Field Attributes
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

Specific attributes can modify how your fields are rendered. Private attributes
start with a `_` and will not be added to the field's attributes. These attributes
can be set in the form class or as an argument like above.

* `_no_label`: Do not show label
* `_no_required`: Do not show required asterisk
* `_no_errors`: Do not show inline errors
* `_inline`: Adds inline class to field
* `_field_class`: Allows for custom field classes
* `_override`: Render as a different input type
* `_style`: Stylize specific fields (BoleanField, ChoiceField)
    * `BooleanField`: set to 'toggle' or 'slider'
    * `ChoiceField`: set to 'search' or 'multiple' and more
* `_icon`: Put icon on field
* `_help`: Display `help_text` if available
* `_align`: Used with `_icon`, which side icon is on; not required

#### Icons
Icons can be added to input fields easily. Add the attribute `_icon` and
optionally `_align` to your arguments.

```html
{% render_field my_form.field _icon='star' _align='left' %}
```

## Custom/Overriding Fields
#### Override to render as different field
Overriding the function that renders the field is done using the `_override`
attribute. This is useful for things like using `CountrySelect` as it is
not its own field type.  


### Custom ChoiceFields

**CountrySelect**  
`CountrySelect` from the `django-countries` package can be used to create a nice
field that displays a list of countries alongside their flags, to access it you
must set the `_override` attribute to `CountrySelect`.

**Icon ChoiceField**  
`IconSelect` can be used with overriding just like `CountrySelect`. This
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
{% render_field my_form.gender _override='IconSelect' %}
```

## Layouts
Using Semantic UI's form layout classes with <i>Semantic UI Forms for Django</i> is simple.  
Within your form's Meta class, simply create a `layout` list. Within that list,
create tuples with an function name as the first value, and the value as the second.  

Functions names are as followed:
* `Text` is for any text or HTML markup. Text in this is considered safe.
* `Field`'s value must be the name of a field.
* `[X] Fields` are containers. It's value must include `Field` items or more
`[X] Field` items. `[X]` should be replaced, either by a number or a class.
All items inside this will be wrapped with a `div` that has the class of the key.
	* `Four Fields`
	* `Six Fields`
	* `Inline Fields`
	* `Equal Width Fields`

To set "wideness" of a specific field, you must add it to the `_field_class`
attribute on your field. It cannot be done in the `layout`.

```python
class ExampleLayoutForm(forms.Form):
	class Meta:
		layout = [
			("Text", "<h4 class=\"ui dividing header\">Personal Details</h4>"),
			("Three Fields",
				("Field", "first_name"),
				("Field", "middle_initial"),
				("Field", "last_name"),
			),

			("Text", "<h4 class=\"ui dividing header\">More Details</h4>"),
			("Inline Fields",
				("Field", "website"),
				("Field", "email"),
			),

			("Text", "<h4 class=\"ui dividing header\">Complicated Details</h4>"),
			("Four Fields",
				("Field", "first_name"),
				("Field", "middle_initial"),
				("Field", "last_name"),
				("Two Fields",
					("Field", "username"),
					("Field", "email"),
				),
			),

			("Field", "helpful")
		]


	username = forms.CharField()
	first_name = forms.CharField()
	middle_initial = forms.CharField()
	last_name = forms.CharField()
	website = forms.CharField()
	email = forms.EmailField()
	phone_number = forms.CharField()
	helpful = forms.BooleanField()
```


## Settings
Override wrappers by finding the wrapper variable name and prepending `SUI_` to it
and inserting it into your `settings.py`.  
```python
SUI_ERROR_WRAPPER = "<div class=\"ui red pointing prompt label\">%(message)s</div>"
```   

You can also change the default placeholder text.
```python
SUI_PLACEHOLDER_TEXT = "Select Option"
```

## Basic Semantic UI Validation Generator
<i>Semantic UI Forms for Django</i> can generate a basic validation configuration for your form. The generator is very basic and does not have many features. It is only intended to give you a starting point.  

View https://semantic-ui.com/behaviors/form.html for more details.

```bash
python manage.py semanticuivalidation app.forms.ExampleForm [--shorthand]
```


## Testing
1. Create a virtual environment.  
```bash
virtualenv -p $(which python3) .env
```

2. Source the activation script.  
```bash
source .env/bin/activate
```

3. Set current directory to `examples` app and then install Python requirements.
```bash
pip install -r requirements.txt
```

4. Make and run migrations for testing purposes.
```bash
python manage.py makemigrations 
python manage.py migrate 
```

5. Run tests.
```bash
python manage.py test semanticuiforms 
```

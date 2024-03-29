from jinja2 import Template

# Create Jinja2 template
j2_template = Template("Hello {{ something }}!!")

# Render template using data
my_output = j2_template.render(something="World")

# Print output
print(my_output)
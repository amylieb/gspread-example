import gspread
import jinja2

gc = gspread.service_account()
sh = gc.open("New Switches")

with open("template.j2") as fh:
    template_str = fh.read()

for ws in sh.worksheets():
    port_list = ws.get_all_records()
    template = jinja2.Template(template_str)
    output = template.render(port_list=port_list)

    with open(f"output/{ws.title}","w") as fh:
        fh.write(output)

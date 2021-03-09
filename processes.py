import wmi 
from collections import defaultdict
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

c = wmi.WMI()
canvas = canvas.Canvas("all_processes.pdf", pagesize=letter)
processes = defaultdict(dict)

# loop through and add all processes to the dict, then sort alphabetically
for process in c.Win32_Process():
    processes[process.Name] = process.ProcessId
processes = dict(sorted(processes.items()))

def create_pdf(canvas, data):
    text = canvas.beginText()
    text.setTextOrigin(inch, inch * 10)

    # add to list and stop if amount of lines exceeds the canvas (more than one A4 page worth)
    for name, id in data.items():
        if text.getY() - inch < 0:
            break
        line = '{} {}'.format(name, id)
        text.textLine(line)

    canvas.drawText(text)
    canvas.save()

def main():
    create_pdf(canvas, processes)

if __name__ == "__main__":
    main()

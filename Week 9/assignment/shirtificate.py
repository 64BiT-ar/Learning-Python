from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

name = input("Enter: ")

pdf.add_page()
# (self, x: float, y: float, text: str = '')
pdf.set_font('helvetica', size=20)
pdf.cell(w=180, h=50, text="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.image("shirt.png", h=100, w=100, x=50, y=50)
pdf.set_font('helvetica', size=14)
pdf.set_text_color(255, 255, 255)
pdf.cell(w=180, h=50, text=f"{name} took CS50", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.output("output.pdf")
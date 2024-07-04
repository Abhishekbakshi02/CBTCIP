from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_receipt(transaction_details, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Payment Receipt")

    # Transaction Details
    c.setFont("Helvetica", 12)
    y = height - 100
    for key, value in transaction_details.items():
        c.drawString(100, y, f"{key}: {value}")
        y -= 20

    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(100, 50, "Thank you for your purchase!")
    c.drawString(100, 35, "If you have any questions, contact us at help@support.com")

    c.save()

transaction_details = {
        "Transaction ID": input("Enter Transaction id :"),
        "Date": input("Enter Date :"),
        "Customer Name": input("Enter name of customer :"),
        "Item Purchased": input("Enter Item purchased :"),
        "Quantity": input("Enter quantity :"),
        "Unit Price": input("Enter unit price :  "),
        "Total Price": input("Enter Total price :")
    }
filename = f"'{transaction_details["Transaction ID"]}'.pdf"
generate_receipt(transaction_details, filename)
print("File saved sucessfully")

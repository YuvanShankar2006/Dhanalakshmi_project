import streamlit as st
from docx import Document
from num2words import num2words
import os
def convert_number_to_words(amount_string: str) -> str:
    amount_int = int(float(amount_string))
    words = num2words(amount_int, lang='en_IN').upper()
    words = words.replace(",", " ").replace("-", " ")
    words = " ".join(words.split())
    return words.upper() + " ONLY"
def replace_in_paragraphs(paragraphs, data):
    for p in paragraphs:
        full_text = "".join(run.text for run in p.runs)
        replaced = full_text
        for key, val in data.items():
            replaced = replaced.replace(f"{{{{{key}}}}}", val)
        if replaced != full_text:
            for run in p.runs:
                run.text = ""
            if p.runs:
                p.runs[0].text = replaced
def generate_bill_docx(data, bill_filename, template_path):
    doc = Document(template_path)
    replace_in_paragraphs(doc.paragraphs, data)

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                replace_in_paragraphs(cell.paragraphs, data)

    for section in doc.sections:
        replace_in_paragraphs(section.footer.paragraphs, data)

    output_path = f"{bill_filename}.docx"
    doc.save(output_path)
    return output_path

st.title("🧾 Bill Generator")

with st.form("bill_form"):
    choice=st.radio("Which company are you generating the Bill For ?",("Yuvan Traders","Dhanalakshmi Traders"))
    bill_no = st.text_input("Bill Number")
    date = st.date_input("Date")
    from_location = st.text_input("From Location")
    to_location = st.text_input("To Location")
    vehicle_no = st.text_input("Vehicle Number")
    qty = st.number_input("Quantity", min_value=1)
    rate = st.number_input("Rate", min_value=1)
    freight = st.number_input("Freight Charges", min_value=0.0, format="%.2f")
    receiver_name = st.text_input("Receiver Name")
    receiver_address = st.text_input("Receiver Address")
    receiver_state = st.text_input("Receiver State")
    receiver_gstin = st.text_input("Receiver GSTIN")
    Eway_bill_no = st.text_input("Eway bill Number")
    is_export = st.radio("Is this an Interstate order?", ("Yes", "No"))
    dd = st.text_input("Distpatchment Details (optional)")  
    submitted = st.form_submit_button("Generate Bill")
if submitted:
    amount = qty * rate
    tamount=amount+freight
    if is_export == "Yes":
        igst_value = tamount * 0.05
        cgst_value = 0
        sgst_value = 0
        cgst=""
        sgst=""
        igst="5%"
    else:
        cgst="2.5%"
        sgst="2.5%"
        igst=""
        igst_value = 0
        cgst_value = tamount * 0.025
        sgst_value = tamount * 0.025
    grand_total = tamount + cgst_value + sgst_value +igst_value
    date_str = date.strftime("%d/%m/%Y")
    total_in_words = convert_number_to_words(str(grand_total))
    if choice=="Dhanalakshmi Traders":
        choice="Dhanalakshmi_new_bill.docx"
    else:
        choice="YuvanTraders_bill.docx"

    data = {
        "receiver_name": receiver_name,
        "receiver_address": receiver_address,
        "receiver_state": receiver_state,
        "receiver_gstin": receiver_gstin,
        "bill_no": str(bill_no),
        "vehicle_no": vehicle_no,
        "date": date_str,
        "from_location": from_location,
        "to_location": to_location,
        "qty": str(qty),
        "rate": f"{rate:.2f}",
        "freight": f"{freight:.2f}",
        "amount": f"{amount:.2f}",
        "tamount": f"{tamount:.2f}",
        "cgst" : cgst,
        "sgst" : sgst,
        "igst" : igst,
        "igst_value": f"{igst_value:.2f}",
        "cgst_value": f"{cgst_value:.2f}",
        "sgst_value": f"{sgst_value:.2f}",
        "grand_total": f"{grand_total:.2f}",
        "Eway_billno": f"{Eway_bill_no}",
        "total_in_words": total_in_words,
        "disp": dd
    }
    filename = f"bill_{bill_no}"
    filepath = generate_bill_docx(data, filename,choice)
    st.success("✅ Bill generated successfully!")

    with open(filepath, "rb") as f:
        st.download_button(
            label="📥 Download Bill (.docx)",
            data=f,
            file_name=os.path.basename(filepath),
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    os.remove(filepath)








### 📄 `README.md`

````markdown
🧾Streamlit Bill Generator using Word Template

This project is a simple and customizable Bill Generator built using **Streamlit** and **python-docx**. It allows users to fill in billing details through a web form and generates a downloadable `.docx` invoice based on a predesigned Word template.

---

 ✅ Features

- Generate professional tax invoices in `.docx` format
- Uses a Word (.docx) template with `{{placeholders}}` for customization
- Supports:
  - Dynamic product data (qty, rate, amount)
  - Tax (CGST, SGST, IGST)
  - Dispatchment details
  - Automatic number-to-words conversion
- Preserves formatting in:
  - Body paragraphs
  - Table cells
  - Footers

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) — for interactive web UI
- [python-docx](https://python-docx.readthedocs.io/en/latest/) — for modifying Word templates
- [num2words](https://pypi.org/project/num2words/) — to convert numbers to words

---

🚀 How to Run

1. **Install required libraries**:

   ```bash
   pip install streamlit python-docx num2words
````

2. **Place your template**:

   * The default Word template should be named:

     ```
     Dhanalakshmi traders1.docx
     ```
   * Use `{{placeholders}}` like `{{receiver_name}}`, `{{amount}}`, etc.

3. **Run the app**:

   ```bash
   streamlit run bill_generator.py
   ```

---

## 📂 Placeholders Expected in the Template

Your Word template should contain these exact placeholders where data will be inserted:

* `{{receiver_name}}`
* `{{receiver_address}}`
* `{{receiver_state}}`
* `{{receiver_gstin}}`
* `{{bill_no}}`
* `{{vehicle_no}}`
* `{{date}}`
* `{{from_location}}`
* `{{to_location}}`
* `{{qty}}`
* `{{rate}}`
* `{{amount}}`
* `{{freight}}`
* `{{tamount}}`
* `{{cgst}}`, `{{cgst_value}}`
* `{{sgst}}`, `{{sgst_value}}`
* `{{igst}}`, `{{igst_value}}`
* `{{grand_total}}`
* `{{Eway_billno}}`
* `{{total_in_words}}`
* `{{disp}}` (e.g. dispatchment details — also works in footer)

---

## 📝 Notes

* The app **supports replacing text inside tables and footers**.
* It **does not** support content inside text boxes, headers, or images.
* Make sure placeholder text (like `{{receiver_address}}`) is **not split across multiple text runs** in Word.
> After filling out the form and submitting, a Word `.docx` invoice is generated and can be downloaded immediately.

---

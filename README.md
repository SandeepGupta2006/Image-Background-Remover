# 🖼️ Image Background Remover App

A simple web application to remove the background from images using the rembg Python module. Built with Flask for the backend and HTML/CSS/JS for the frontend.

---

## 🔧 Features

- 📤 Upload image from your device
- ✂️ Remove background locally (no API or internet needed)
- 📥 Download the processed image
- ⚙️ Fast and private — no external API calls
- 🖥️ Built with Flask, rembg, HTML/CSS/JavaScript

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, [rembg](https://pypi.org/project/rembg/)
- **Frontend**: HTML, CSS, JavaScript
- **Libraries**: `Pillow` for image handling

---

## ⚙️ Installation

To run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/SandeepGupta2006/Image-Background-Remover.git
cd Image-Background-Remover

# 2. (Optional) Create a virtual environment
python -m venv venv
# Activate it
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
flask run
```
---

## 🔐 Privacy Note

This app runs entirely on your machine — no image data is sent to external servers or APIs.  
All image processing is done locally using `rembg`.  
Your uploads stay private and are not stored or shared.

---

## 🙋‍♂️ Author

**Sandeep Gupta**
[Portfolio](https://github.com/) • [GitHub](https://github.com/SandeepGupta2006/) • [LinkedIn](https://www.linkedin.com/in/sandeep-gupta-5872b4315/)

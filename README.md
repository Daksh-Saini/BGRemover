# 🖼️ Image Background Remover

A simple web app built with Streamlit to easily remove backgrounds from your images using the `rembg` library.
*(**Note:** You should replace the link above with a screenshot of your running application)*

---

## 🚀 Features

* **Simple UI:** Clean and easy-to-use interface.
* **File Upload:** Upload your PNG images directly in the app.
* **Side-by-Side View:** Instantly compare the original image with the processed result.
* **One-Click Processing:** Remove the background with a single button click.
* **Download Result:** Download the final image with a transparent background, automatically named `{original_filename}_no_bg.png`.

## 🛠️ Technologies Used

* **Python:** The core programming language.
* **Streamlit:** For building the interactive web application.
* **rembg:** A powerful Python library for removing image backgrounds.
* **Pillow (PIL):** For image opening, processing, and saving.

## 🏃 How to Run Locally

Follow these steps to get the application running on your local machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name
```

### 2. Create a Virtual Environment (Recommended)

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

You'll need a `requirements.txt` file. You can create one with the content below:

**`requirements.txt`**
```
streamlit
rembg
Pillow
onnxruntime
```

Now, install the requirements:
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

Save your Python code as `app.py` in the main directory. Then run:

```bash
streamlit run app.py
```

Open your web browser and go to `http://localhost:8501` to use the app.
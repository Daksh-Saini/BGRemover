import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import os

# Set page configuration
st.set_page_config(layout="wide", page_title="Image Background Remover")

#  App Title and Description 
st.title("🖼️ Image Background Remover")
st.info("Upload your image, click 'Remove Background', and download the result!")
st.markdown("---")

#  Sidebar Instructions 
st.sidebar.header("How to Use")
st.sidebar.markdown(
    """
    1.  **Upload** an image using the 'Choose an image...' button.
    2.  The original image will be displayed.
    3.  Click the **'Remove Background'** button.
    4.  The processed image will appear in the 'Result' section.
    5.  Click the **'Download Image'** button to save it.
    """
)
st.sidebar.markdown("")
#  Main App Layout (Input and Output Columns) 
col1, col2 = st.columns(2)
with col1:
    st.header("Your Image 🖼️")
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["png"])
    if uploaded_file is not None:
        # Read the uploaded file as a PIL Image
        try:
            inp_image = Image.open(uploaded_file)
            st.image(inp_image, caption="Original Image", use_column_width=True)
            # Button to trigger background removal
            process_button = st.button("✨ Remove Background", use_container_width=True, type="primary")
        except Exception as e:
            st.error(f"Error opening image: {e}")
            process_button = False # Ensure button doesn't exist if image fails
    else:
        st.info("Please upload an image to get started.")
        process_button = False
with col2:
    st.header("Result 🪄")
    if process_button and 'inp_image' in locals():
        # Show a spinner while processing
        with st.spinner("Processing... Please wait."):
            try:
                # Process the image using rembg
                output_image = remove(inp_image)
                st.image(output_image, caption="Background Removed", use_column_width=True)
                #  Download Button Logic 
                # Convert PIL Image to bytes
                buf = BytesIO()
                output_image.save(buf, format="PNG")
                byte_im = buf.getvalue()
                
                # Get the original filename without extension
                original_filename = os.path.splitext(uploaded_file.name)[0]
                download_filename = f"{original_filename}_no_bg.png"
                
                st.download_button(
                    label="📥 Download Image",
                    data=byte_im,
                    file_name=download_filename,
                    mime="image/png",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"An error occurred during background removal: {e}")
    
    elif process_button:
        # This case handles clicking the button without an image
        st.warning("Please upload an image first.")
    else:
        st.info("Your processed image will appear here.")

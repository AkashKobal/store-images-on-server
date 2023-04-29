import os
from PIL import Image

if "submit" in request.form:
    target_dir = "Image-Folder/"
    target_file = target_dir + secure_filename(request.files["fileToUpload"].filename)
    upload_ok = 1
    image_file_type = os.path.splitext(target_file)[1].lower()

    # Check if image file is a actual image or fake image
    if request.files["fileToUpload"].filename != "":
        if not Image.open(request.files["fileToUpload"].stream):
            print("File is not an image.")
            upload_ok = 0

    # Check if file already exists
    if os.path.isfile(target_file):
        print("Sorry, file already exists.")
        upload_ok = 0

    # Check file size
    # 500,000 bytes (which is approximately 500 kilobytes).
    if request.files["fileToUpload"].content_length > 500000:
        print("Sorry, your file is too large.")
        upload_ok = 0

    # Allow certain file formats
    if image_file_type not in (".jpg", ".png", ".jpeg", ".gif"):
        print("Sorry, only JPG, JPEG, PNG & GIF files are allowed.")
        upload_ok = 0

    # Check if upload_ok is set to 0 by an error
    if upload_ok == 0:
        print("Sorry, your file was not uploaded.")
    else:
        request.files["fileToUpload"].save(target_file)
        print(f"The file {request.files['fileToUpload'].filename} has been uploaded.")

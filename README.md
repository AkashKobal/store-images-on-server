# store-images-on-server
Algorithm-and-Code-to-store-images-on-server


README

Before saving a file to a specified directory, this Python script verifies that the file is a valid image and complies with certain specifications.

You must have the following dependencies installed in order to use this script:
- The Pillow library (PIL) for Python 3.x

Navigate to the script's directory in a command prompt or terminal and type "python filename.py" to start the script. 'filename' should be changed to the name of the script file.

If a file is submitted and satisfies the following criteria, the script accepts it and saves it to a designated directory.
- The image in the file is real.
- The file is not already present in the directory that was given.
- The file's size is limited to 500,000 bytes, or around 500 kilobytes.

- The file's format is JPG, JPEG, PNG, or GIF.

The file is not saved if any of these conditions are not satisfied, and an error message is shown instead.

It should be noted that this script presupposes that the file is being uploaded via a web form and that the'request' object is accessible to access the uploaded file. This script needs to be adjusted if you plan to use it in a different situation.

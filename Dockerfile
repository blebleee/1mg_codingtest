FROM rackspacedot/python37
RUN apt-get update && apt-get install -y tesseract-ocr \
    ffmpeg libsm6 libxext6 
ADD . . 
RUN pip3 install -r requirements.txt
CMD ["python", "main.py"]

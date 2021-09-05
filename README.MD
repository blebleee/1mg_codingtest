# 1MG Coding challenge

## Source code
https://github.com/blebleee/1mg_codingtest


## What's inside
- A website to recognize the handwritten digits uploaded by users
- Using an opensource tool Tesseract: https://github.com/madmaze/pytesseract


## Installation guide

In order to install this product, kindly choose 1 of the following 2 options:

### Option 1: Using Docker

#### Prerequisite: 
- Docker installed in the local machine
- git installed in the local machine

#### Steps:
1. Clone the source code
- This step will do get the source code from github to your local machine

```bash
git clone https://github.com/blebleee/1mg_codingtest
cd 1mg_codingtest
```
2. Build the docker image
- This step will do build a dockerfile
- Remember to enter root password in order to run sudo
  
```bash
sudo docker build -t mnisting .
```
3. Run the server using docker
```bash
sudo docker run -itd -p 8888:8888 --name mnist mnisting:latest
```

### Option 2: Using the source code
```bash
pip install -r requirements.txt
python3 main.py
```


## Usage guide
- In order to use the product, please
  - Prepare some handwritten images
  - Open your web browser
  - Enter `localhost:8888` 
  - Upload images with "select" button then predict with "submit" button.
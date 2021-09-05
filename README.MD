# 1mg markdown

# 1MG take home coding test

This is my work for MNISTING project. The website look like this

![Screenshot from 2021-09-05 00-32-03.png](1mg%20markdown%20cb6733966140407d8c86b4ab87307735/Screenshot_from_2021-09-05_00-32-03.png)

### Installation

```bash
git clone https://github.com/blebleee/1mg_codingtest
cd 1mg_codingtest
```

1. Docker images

```bash
sudo docker build -t mnisting .
sudo docker run -itd -p 8888:8888 --name mnist mnisting:latest
```

1. From source

```bash
pip install -r requirments.txt
python3 main.py
```

### Usage

Enter `localhost:8888` in your browser, select the images that you want to predict then press submit button.
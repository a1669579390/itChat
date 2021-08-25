FROM python:3.6.4


WORKDIR /code
COPY requirements.txt .
RUN pip install -r /code/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["/bin/bash","run.sh"]
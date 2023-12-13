FROM python:3.9

# image workdir
WORKDIR /data/cellxgene-gateway/

# add project to the image
COPY . /data/cellxgene-gateway/

RUN python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip config set global.extra-index-url "https://mirrors.aliyun.com/pypi/simple https://pypi.tuna.tsinghua.edu.cn/simple"

RUN pip install -r /data/cellxgene-gateway/requirements.txt

ENV CELLXGENE_DATA=/cellxgene-data
ENV CELLXGENE_LOCATION=/usr/local/bin/cellxgene

CMD ["python", "gateway.py"]

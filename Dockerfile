FROM python:2.7
ADD pull.py /
RUN pip install paho-mqtt
RUN pip install pymongo

CMD ["python", "./pull.py"]

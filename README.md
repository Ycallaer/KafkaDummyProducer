# Kafka Dummy Producer

## Goal of the repo
The goal is to demonstrate a kafka producer in python using the confluent kafka library.
We are using the gunviolence data which can be found on kaggle (I am using a small subset).

I also use this program to check if new clusters can process incoming data.

## Prerequiste
You will need to install the following to get going with this project

* [librdkafka](https://github.com/edenhill/librdkafka)
* python 3.X
* confluent kafka
* arrow

## Getting started
Install the prerequisites
When you are done, do not forget to change the broker ip in the config class.
If you want to use localhost do not forgot to port forward the cluster ip:port

### 1. Build docker images and upload to repo
If you are working with an ide, the starting point is in GenerateKafkaMsg.py

import confluent_kafka
from dummyproducer.Config.configuration import getConfigForEnv

class CustomKafkaProducer:
    def __init__(self):
        self.config = getConfigForEnv("local")
        self.topic_name = self.config["kafka_produce_topic"]

        conf = {'bootstrap.servers': self.config["bootstrap_servers"],
                'message.max.bytes': self.config["kafkaMaxMessageBytes"],
                'queue.buffering.max.ms': self.config["queue.buffering.max.ms"],
                'queue.buffering.max.messages': self.config["queue.buffering.max.messages"]
                }

        self.producer = confluent_kafka.Producer(**conf)

    def on_delivery(self, err, msg):
        if err:
            print("Message failed delivery, error: %s", err)
        else:
            print("Message delivered to %s on partition %s", msg.topic(), msg.partition())


    def produce(self, kafka_msg, kafka_key):
        try:
            self.producer.produce(topic=self.topic_name,
                                  value=kafka_msg,
                                  key=kafka_key,
                                  callback=lambda err, msg: self.on_delivery(err, msg)
            )

            self.producer.flush()

        except Exception as e:
            print("Error during producing to kafka topic. Stacktrace is %s",e)

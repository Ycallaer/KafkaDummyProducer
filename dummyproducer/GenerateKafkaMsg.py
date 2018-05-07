from dummyproducer.CustomKafkaProducer.CustomKafkaProducer import CustomKafkaProducer
import arrow

def startKakfkaProducer():
    print("Initializing the kafka producer")
    producer=CustomKafkaProducer()
    filepath="../resources/gunviolence.csv"

    with open(filepath,'r') as filep:
        cnt=0
        for line in filep:
            if cnt==0:
                print("skipping the header")
                cnt=cnt+1
            else:
                print(line)
                utc = str(arrow.now().timestamp)
                producer.produce(kafka_msg=line,kafka_key=utc)

if __name__=="__main__":
    startKakfkaProducer()
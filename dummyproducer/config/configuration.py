config = {
    'local': {
        'bootstrap_servers': 'localhost:9093',
        'kafkaMaxRequestSize': 50331648,
        'kafkaMaxMessageBytes': 50331648,
        'kafka_produce_topic': 'GunViolence',
        'fetch.wait.max.ms': 60000,
        'session.timeout.ms': 180000,
        'heartbeat.interval.ms': 60000,
        'queue.buffering.max.ms': 1,
        'queue.buffering.max.messages': 1000
    }
}

def getConfigForEnv(environment):
    return config[environment]
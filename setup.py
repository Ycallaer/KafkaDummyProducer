try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'Yves Callaert'

setup(
    name="KafkaDummyProducer",
    description="KafkaDummyProducer",
    version="0.0.1",
    packages=["dummyproducer", "dummyproducer.config", "dummyproducer.customkafkaproducer"],
    scripts=[],
    install_requires=[
        'confluent_kafka==0.11.0', 'arrow==0.12.1'
    ],
    dependency_links=[]
)

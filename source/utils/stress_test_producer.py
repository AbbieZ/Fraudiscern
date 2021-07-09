# -*- coding: utf-8 -*-
"""
# Name: stress_test_producer.py
# Developer: Zhang Siyu
# Data: 23.06.2021
# Version: v1
"""

import time

import kafka_manager
from data_generator import generate_transaction_data


def stress_test_kafka_producer(start_date="1-1-2012", end_date="1-31-2012", frequency=0.1):
    """Send transaction data to kafka cluster as a producer client

    """
    producer = kafka_manager.get_kafka_producer()
    transaction_data_set = generate_transaction_data(start_date=start_date, end_date=end_date)
    for index, row in transaction_data_set.iterrows():
        # Send a piece of transaction every 0.1 second.
        data = row.to_json()
        time.sleep(frequency)
        producer.send(topic='test_data', value=data)
        print("{} has been send".format(data))
    return None


stress_test_kafka_producer()

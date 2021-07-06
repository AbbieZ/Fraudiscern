# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@file: kafka_manager.py
@time: 7/4/2021
@version:
"""
import json

from kafka import KafkaConsumer
from kafka import KafkaProducer


def get_kafka_producer():
    """[summary]

    Returns:
        [type]: [description]
    """
    # 实例化一个KafkaProducer示例，用于向Kafka投递消息
    producer = _create_kafka_producer()
    return producer


def _create_kafka_producer():
    """[summary]

    Returns:
        [type]: [description]
    """
    kafka_producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                   bootstrap_servers=['spark-797d5ccdb-2d4wd', 'spark-797d5ccdb-2jmdw',
                                                      'spark-797d5ccdb-4sq79', 'spark-797d5ccdb-6hsdc',
                                                      'spark-797d5ccdb-72z2j', 'spark-797d5ccdb-9qz5w',
                                                      'spark-797d5ccdb-c56g9', 'spark-797d5ccdb-csq2m',
                                                      'spark-797d5ccdb-fjmbr', 'spark-797d5ccdb-h2hcq',
                                                      'spark-797d5ccdb-ht7vz', 'spark-797d5ccdb-kvsrm',
                                                      'spark-797d5ccdb-l7txm', 'spark-797d5ccdb-ln2xr',
                                                      'spark-797d5ccdb-m6ctm', 'spark-797d5ccdb-m92qw',
                                                      'spark-797d5ccdb-n2sr7', 'spark-797d5ccdb-p86qx',
                                                      'spark-797d5ccdb-ph9lc', 'spark-797d5ccdb-pzz6s',
                                                      'spark-797d5ccdb-r78mv', 'spark-797d5ccdb-rjb6h',
                                                      'spark-797d5ccdb-s2hb2', 'spark-797d5ccdb-s7fw6',
                                                      'spark-797d5ccdb-s8jdd', 'spark-797d5ccdb-vp48k',
                                                      'spark-797d5ccdb-vt9c7', 'spark-797d5ccdb-x84dm',
                                                      'spark-797d5ccdb-xbwtr', 'spark-797d5ccdb-xwtgf',
                                                      'spark-797d5ccdb-zgsg4', 'spark-797d5ccdb-zsk59']
                                   )
    return kafka_producer


def get_kafka_consumer():
    """return a kafka consumer instance

    """

    consumer = _create_kafka_consumer()
    return consumer


def _create_kafka_consumer():
    """[summary]

    Returns:
        [type]: [description]
    """
    kafka_consumer = KafkaConsumer('test_data', bootstrap_servers=['spark-797d5ccdb-2d4wd', 'spark-797d5ccdb-2jmdw',
                                                                   'spark-797d5ccdb-4sq79', 'spark-797d5ccdb-6hsdc',
                                                                   'spark-797d5ccdb-72z2j', 'spark-797d5ccdb-9qz5w',
                                                                   'spark-797d5ccdb-c56g9', 'spark-797d5ccdb-csq2m',
                                                                   'spark-797d5ccdb-fjmbr', 'spark-797d5ccdb-h2hcq',
                                                                   'spark-797d5ccdb-ht7vz', 'spark-797d5ccdb-kvsrm',
                                                                   'spark-797d5ccdb-l7txm', 'spark-797d5ccdb-ln2xr',
                                                                   'spark-797d5ccdb-m6ctm', 'spark-797d5ccdb-m92qw',
                                                                   'spark-797d5ccdb-n2sr7', 'spark-797d5ccdb-p86qx',
                                                                   'spark-797d5ccdb-ph9lc', 'spark-797d5ccdb-pzz6s',
                                                                   'spark-797d5ccdb-r78mv', 'spark-797d5ccdb-rjb6h',
                                                                   'spark-797d5ccdb-s2hb2', 'spark-797d5ccdb-s7fw6',
                                                                   'spark-797d5ccdb-s8jdd', 'spark-797d5ccdb-vp48k',
                                                                   'spark-797d5ccdb-vt9c7', 'spark-797d5ccdb-x84dm',
                                                                   'spark-797d5ccdb-xbwtr', 'spark-797d5ccdb-xwtgf',
                                                                   'spark-797d5ccdb-zgsg4', 'spark-797d5ccdb-zsk59'])
    return kafka_consumer

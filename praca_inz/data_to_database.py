#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

import time
from datetime import datetime

from bme280 import BME280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

mydb = mysql.connector.connect(
  host="localhost",
  user="micgab",
  password="haslo",
  database="TestDB3"
)

def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

factor = 1.3

cpu_temps = [get_cpu_temperature()] * 5


while True:
    cpu_temp = get_cpu_temperature()
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
    raw_temp = bme280.get_temperature()
    comp_temp = raw_temp - ((avg_cpu_temp - raw_temp) / factor)

    temperature = comp_temp
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    date_and_time = datetime.now()
    mycursor = mydb.cursor()

    sql = "INSERT INTO weather_station_sensor (temperature,pressure,humidity,date) VALUES (%s, %s, %s, %s)"
    val = (round(temperature,2), round(pressure,2), round(humidity,2), date_and_time)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    time.sleep(900)

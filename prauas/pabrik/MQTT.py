from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt

from .serializers import ActuatorSerializer, SensorSerializer
from .models import Actuator, Sensor


def run_mqtt():
    client = mqtt.Client("DjangoApp")

    client.message_callback_add("farm/kandang/temperatur", update_kot)
    client.message_callback_add("farm/kandang/kelembaban", update_kog)
    client.message_callback_add("farm/kandang/pakan", update_kor)

    client.message_callback_add("farm/wagyu/berat", update_kct)
    client.message_callback_add("farm/wagyu/kualitas", update_kcc)
    client.message_callback_add("farm/wagyu/lemak", update_kcr)

    client.message_callback_add("farm/ikan/berat", update_ket)
    client.message_callback_add("farm/ikan/lemak", update_kek)
    client.message_callback_add("farm/ikan/panjang", update_ker)

    client.connect('localhost', 1883)
    client.loop_start()
    client.subscribe("farm/kandang/temperatur")
    client.subscribe("farm/kandang/kelembaban")
    client.subscribe("farm/kandang/pakan")

    client.subscribe("farm/wagyu/berat")
    client.subscribe("farm/wagyu/kualitas")
    client.subscribe("farm/wagyu/lemak")

    client.subscribe("farm/ikan/berat")
    client.subscribe("farm/ikan/lemak")
    client.subscribe("farm/ikan/panjang")

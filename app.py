import streamlit as st
from kafka import KafkaConsumer
import json

# Configurar la página de Streamlit
st.set_page_config(page_title="Monitor de Kafka", layout="wide")

st.title("📊 Monitor de Kafka en Tiempo Real")

# Configurar el consumidor de Kafka
KAFKA_BROKER = "kafka:9092"
TOPIC = "test-topic"  # Cambia esto por el tema correcto

try:
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset="earliest",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )
    st.success(f"📡 Conectado al broker {KAFKA_BROKER} y al topic '{TOPIC}'")
except Exception as e:
    st.error(f"❌ Error al conectar con Kafka: {e}")
    consumer = None

# Mostrar mensajes en tiempo real
st.subheader("📥 Mensajes recibidos:")
message_placeholder = st.empty()

if consumer:
    for message in consumer:
        message_placeholder.text(f"📩 {message.value}")


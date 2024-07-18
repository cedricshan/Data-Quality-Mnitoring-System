import logging
from .data_loader import load_data
from .anomaly_detector import detect_anomalies
from .alert import send_alert
from config.config import LOG_PATH

def setup_logging():
    logging.basicConfig(filename=LOG_PATH, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    setup_logging()
    data = load_data()
    anomalies = detect_anomalies(data)
    
    if anomalies:
        logging.warning(f"Anomalies detected: {anomalies}")
        send_alert(anomalies)
    else:
        logging.info("No anomalies detected.")

if __name__ == "__main__":
    main()

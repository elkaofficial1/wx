import yaml
import os

def load_config(config_path='config.yml'):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    
    return config

def Load_API():
    config = load_config()
    return config["weather_settings"]["API_WEATHER"]

def load_sity():
    config = load_config()
    return config["weather_settings"]["CITY"]

def Load_lang():
    config = load_config()
    return config["application"]["LANG"]




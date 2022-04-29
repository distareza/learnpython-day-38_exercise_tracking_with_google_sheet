import configparser

config = configparser.RawConfigParser()
config.read(filenames="../config.properties")

nutritionix_app_id = config.get("nutritionix.com", "nutritionix.application.id")
nutritionix_app_key = config.get("nutritionix.com", "nutritionix.application.key")

sheet_endpoint = config.get("sheety.co", "sheety.endpoint.url")
sheet_token = config.get("sheety.co", "sheety.token")
from datetime import date
from dotenv import dotenv_values
import tweepy as tp
import logging

logging.basicConfig(level=logging.INFO, filename="bot_log.txt",
                    format='%(asctime)s :: %(levelname)s :: %(message)s')

config = dict(dotenv_values(".env"))

# Connect to twitter api
auth = tp.OAuthHandler(config['API_KEY'], config['API_KEY_SECRET'])
auth.set_access_token(config['ACCESS_TOKEN'], config['ACCESS_TOKEN_KEY'])

api = tp.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

today = date.today()
last_day_of_year = date(2021,12,31)

delta = last_day_of_year - today

message = f"Il reste {delta.days} jours avant la fin de l'année."

if (delta.days == 0):
    message = "C'est le dernier jour de l'année"

try:
    logging.info("Updating status")
    api.update_status(message)
    logging.info("End updating status")
except tp.TweepError as error:
    if error.api_code == 187:
        logging.error("Duplicate status")
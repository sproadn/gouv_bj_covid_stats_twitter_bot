#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Desc: Obtenez les dernières statistiques du Bénin sur le coronavirus
# Author: https://twitter.com/SperoAdonon
#
from dotenv import dotenv_values
from covid_stat import get_gouv_bj_covid_stats
import tweepy as tp
import time
import logging

logger = logging.getLogger()
config = dict(dotenv_values(".env"))

# Connect to twitter api
auth = tp.OAuthHandler(config['API_KEY'], config['API_KEY_SECRET'])
auth.set_access_token(config['ACCESS_TOKEN'], config['ACCESS_TOKEN_KEY'])

api = tp.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

status_message = get_gouv_bj_covid_stats()

# update twitter status
api.update_status(status_message)

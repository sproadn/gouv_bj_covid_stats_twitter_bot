#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Desc: Obtenez les dernières statistiques du Bénin sur le coronavirus
# Author: https://twitter.com/SperoAdonon
#
import requests
from bs4 import BeautifulSoup
import sys
import datetime



def get_gouv_bj_covid_stats():
	gouvbjpage = requests.get("https://www.gouv.bj/coronavirus/")
	soup = BeautifulSoup(gouvbjpage.content, 'html.parser')
	all_stats = soup.find_all('h2', class_="h1 adapt white left-5")
	cas = []
	for stat in all_stats:
		cas.append(stat.get_text())

	cas_confirme = f"Cas confirmés\t: {cas[0]}\n"
	sous_traitement = f"Sous traitement\t: {cas[1]}\n"
	cas_gueris = f"Cas guéris\t: {cas[2]}\n"
	deces = f"Décès\t: {cas[3]}\n"
	#date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	source = f"Source: https://gouv.bj/coronavirus \n"
	conseil = "\nPrenez soins de vous et respectez les gestes barrières.\n"

	message = cas_confirme + sous_traitement + cas_gueris + deces + source + conseil

	with open('message.txt', 'w') as message_file:
		message_file.write(message)

	return message

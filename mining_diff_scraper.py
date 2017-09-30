#! python3
# mining_diff_scraper - scrapes whattomine.com for historical mining difficulty
# nethash and other relevant data for crypto currencies

import json
import requests
import pandas as pd
import time



# Print main coin and current difficulty
def get_coin():

	coin = coin_data['tag']
	difficulty = coin_data['difficulty']
	print('The Current Difficulty of ' + coin + ' is ' + str(difficulty))
	timestamp = coin_data['timestamp']


# Full info of main coin 
def full_info():
	info = pd.Series(coin_data)
	print(info)


# Get LBC dataframe and save to spreadsheet
def LBC_to_csv():
	lbryjson = pd.read_json(LBC.content, typ='series')
	LBC_df = pd.DataFrame(lbryjson)
	LBC_df.to_csv('E:\code\python\death916\mining-difficulty\Lbry_History.csv', mode='a')
	print('saved LBC data to spreadsheet')




# TODO this is a test
while True:

	
	
	try:
		LBC = requests.get('http://whattomine.com/coins/164.json')

		if LBC.status_code == requests.codes.ok:
			print('Loaded coin data')
		else:
			print('Could not load coin data')
	except:
		print('could not load coin data')

	coin_data = json.loads(LBC.text)
	
	get_coin()
	full_info()
	LBC_to_csv()
	time.sleep(500)




"""
allcoins = requests.get('http://whattomine.com/coins.json')
#alldata = json.loads(allcoins.text)
alldata = pd.read_json(allcoins.text)


#print(all_coin_tags)


print(alldata)
"""
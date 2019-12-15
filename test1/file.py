import os

if not os.path.exists('extras'):
	os.system('git clone https://github.com/ARACADERISE/extras')

os.system('cd extras/python/yal_lang && ls')

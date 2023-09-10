import argparse
import wave
from argparse import RawTextHelpFormatter
import numpy as np
from scipy.io import wavfile
from termcolor import colored
from dolphinido.dolphinido import Dolphinido

dolphinido = Dolphinido()

def fingerprint(args):
	audio_file = args.fingerprint[0]
	try:
		result = dolphinido.create_audio(audio_file)
		if result:
			print(colored("Operation successful", "green"))		
	except Exception as err:
		print(colored(str(err), "red"))

def radio(args):
	station = args.radio[0]
	try:
		radio = dolphinido.radio()
		radio.tune(float(station))
		radio.play()
	except Exception as err:
		print(colored(str(err), "red"))

def recognize_file(args):
	match = None
	audio_file = args.recogfile[0]
	try:
		match = dolphinido.recognize_file(audio_file)
	except Exception as err:
		print(colored(str(err), "red"))
	output(match)

def recognize_audio(args):
	match = None
	duration = args.recogmic[0]
	try:	
		match = dolphinido.recognize_recording(duration)
	except Exception as err:
		print(colored(str(err), "red"))
	output(match)

def recognize_radio(args):
	match = None
	station = args.recogradio[0]
	try:	
		radio = dolphinido.radio()
		radio.tune(float(station))
		samples = radio.capture(1024*20*1000)
		match = dolphinido.recognize_audio(samples)
	except Exception as err:
		print(colored(str(err), "red"))
	output(match)

def input():
	ps = argparse.ArgumentParser(
		description="Dolphinido Audio Fingerprint",
		formatter_class=RawTextHelpFormatter
	)
	
	ps.add_argument(
		'--radio', nargs=1,
		help='Listen to Radio. Usage: \n'
		     '--radio station \n'
	)

	ps.add_argument(
		'--fingerprint', nargs=1,
		help='Fingerprint audio file. Usage: \n'
		     '--fingerprint path/to/file \n'
	)

	ps.add_argument(
		'--recogfile', nargs=1,
		help='Recognize audio from file. Usage: \n'
		     '--recogfile path/to/file \n'
	)
	
	ps.add_argument(
		'--recogmic', nargs=1,
		help='Recognize audio from microphone. Usage: \n'
		     '--recogmic seconds \n'
	)

	ps.add_argument(
		'--recogradio', nargs=1,
		help='Recognize audio from radio station. Usage: \n'
		     '--recogradio station \n'
	)

	return ps

def output(match):
	if match:
		msg = 'Match Found \n \n'
		msg += 'Audio ID: %s \n'
		msg += 'Title: %s \n'
		msg += 'Artist: %s \n'
		msg += 'Offset: %d \n'
		msg += 'Offset Seconds : %d secs \n'
		msg += 'Confidence: %d'

		print("#" * 40)
		print(colored(msg, 'green') % (
			match.audio.id,
			match.audio.metadata.title,
			match.audio.metadata.artist,
			match.offset,
			match.offset_seconds,
			match.confidence
		))
		print("#" * 40)
	else:
		msg = ' ** No matches found'
		print(colored(msg, 'red'))


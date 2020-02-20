from subprocess import check_call, CalledProcessError
import re
import argparse
import json
import requests
import time

def compute_face_recognition_results(profile_id):
	profile_file_location = ("/tmp/face-recognition/%s.log" % profile_id)
	profile_id_found = []
	no_face_found_count = 0
	total_captures = 0
	profile_id_captures = 0
	other_profiles_captured = 0
	no_face_weight = 0.2
	profile_face_found_weight = 1
	other_profile_found_weight = 0.1

	with open(profile_file_location) as profile_file:
		for line in profile_file:
			# profile_log = line.strip().split("|")[1]
			# result = re.search('profile_id (.*) found', profile_log.strip())
			# profile_id_found.append(result.group(1)) 
			total_captures += 1
			if line.strip() == 'NO_FACE_FOUND':
				no_face_found_count += 1
			else:
				if line.strip() == profile_id:
					profile_id_captures += 1
				else:
					other_profiles_captured += 1
				profile_id_found.append(line.strip())
	attention_percentage = (no_face_found_count * no_face_weight + profile_id_captures * profile_face_found_weight + other_profiles_captured * other_profile_found_weight) * 100/total_captures
	profile_ids_list = set(profile_id_found)
	# print(profile_ids_list)
	other_profiles_found = list(set(profile_id_found))
	other_profiles_found.remove("%s" % profile_id)
	face_recognition_result = {}
	face_recognition_result['eid'] = "DC_PROCTOR"
	face_recognition_result['stallId'] = "STA3"
	face_recognition_result['ideaId'] = "IDE23"
	face_recognition_result['profileId'] = profile_id
	edata = {}
	edata['attention_percentage'] = round(attention_percentage, 2)
	# face_recognition_result['player_profile_id'] = profile_id
	edata['anon_profile_ids'] = other_profiles_found
	edata['total_frames_captured'] = total_captures
	face_recognition_result['edata'] = edata
	face_recognition_result['ets'] = int(time.time())

	### Request envelope to call telemetry api
	request_envelope = {}
	request_envelope['id'] = "api.devcon.sunbirded.telemetry"
	request_envelope['ver'] = "3.0"
	params = {"msgid": "7e7a3aa5e1954bb019f17032517e2b0e"}
	request_envelope['ets'] = int(time.time())
	events = []
	events.append(face_recognition_result)
	request_envelope['events'] = events
	output_json = json.dumps(request_envelope)
	print(output_json)
	res = requests.post('https://devcon.sunbirded.org/content/data/v1/telemetry', json=request_envelope)
	print(res.text)

def stop_detection(args):
	try:
		check_call(["pkill", "-9", "-f", "face_recognition.py"])
	except CalledProcessError as err:
		print("Face recognition process was already killed")
		print(err)
	compute_face_recognition_results(args.profile_id)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("profile_id", type=str, help="User profile being monitored")
  stop_detection(parser.parse_args())
from subprocess import check_call, CalledProcessError
import re
import argparse
import json

def compute_face_recognition_results(args):
	profile_file_location = ("/tmp/face-recognition/%s.log" % args.profile_id)
	profile_id_found = []
	with open(profile_file_location) as profile_file:
		for line in profile_file:
			profile_log = line.strip().split("|")[1]
			result = re.search('profile_id (.*) found', profile_log.strip())
			profile_id_found.append(result.group(1)) 
	profile_ids_list = set(profile_id_found)
	other_profiles_found = list(set(profile_id_found))
	other_profiles_found.remove("%s" % args.profile_id)
	face_recognition_result = {}
	face_recognition_result['player_profile_id'] = args.profile_id
	face_recognition_result['other_profile_ids_found'] = other_profiles_found
	output_json = json.dumps(face_recognition_result)
	print(output_json)

def stop_face_recognition(args):
	try:
		check_call(["pkill", "-9", "-f", "face-recognition.py"])
	except CalledProcessError as err:
		print("Face recognition process was already killed")
		print(err)
	compute_face_recognition_results(args)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("profile_id", type=str, help="User profile being monitored")
  stop_face_recognition(parser.parse_args())
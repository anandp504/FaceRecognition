from flask import Flask, render_template, request, jsonify, Response

from face_recognition import start_face_recognition as recognize
from stop_face_recognition import stop_detection
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
pool = ThreadPoolExecutor(3)

@app.route('/devcon/face_recognition/start/<profile_id>', methods=['POST'])
def start_face_recognition(profile_id):
    print("Starting face recognition for %s " % profile_id)
    try: 
        #face_app_process = Process(target=recognize, args=(profile_id, True))
        #face_app_process.start()
        #face_app_process.join()
        #pool.submit(recognize, (profile_id, True))
        recognize(profile_id, True)
        return Response('{"response": "Face recognition started"}', status = 200, mimetype='application/json')
    except Exception as err:
        print("Something failed: Druid connection failed")
        print(err)
        raise

@app.route('/devcon/face_recognition/stop/<profile_id>', methods=['POST'])
def stop_face_recognition(profile_id):
    print("Stopping face recognition for %s " % profile_id)
    try: 
        stop_detection(profile_id)
    except Exception as err:
        print("Something failed: Druid connection failed")
        print(err)
        raise

if __name__ == '__main__':
    app.run(debug=True)
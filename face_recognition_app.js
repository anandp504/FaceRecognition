// import express JS module into app 
// and creates its variable. 

var express = require('express'); 
var bodyParser = require('body-parser')
var app = express(); 
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
  
app.listen(5000, function() { 
    console.log('server running on port 5000'); 
} ) 

app.post('/devcon/face_recognition/start', startFaceRecognition); 
  
function startFaceRecognition(req, res) { 
    var spawn = require("child_process").spawn;  
    var process = spawn('python',["/Users/anand/Documents/code/FaceRecognition/face_recognition.py", 
                            req.query.profile_id] ); 
  
    res.send('{"response": "Successfully started face recognition"'); 
    
    /*
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    }); 
    */
} 

app.post('/devcon/face_recognition/stop', stopFaceRecognition); 
  
function stopFaceRecognition(req, res) { 
    var spawn = require("child_process").spawn;  
    var process = spawn('python',["/Users/anand/Documents/code/FaceRecognition/stop_face_recognition.py", 
                            req.query.profile_id] ); 
  
    res.send('{"response": "Successfully started face recognition"'); 
    
    /*
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    }); 
    */
} 
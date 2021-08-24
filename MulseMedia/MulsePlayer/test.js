
var engineAddress = "127.0.0.1:49676";  //this can be found in coreProps.json file it changes when the computer is restarted
var duration = 0;
var startOlf = 0;
var fanNum = 1;
var playing = true;
var interval;

count = 1;

var start = function(){
  JSONfuncHaptic();
  JSONfunc();
}

var JSONfunc = function () {
   var  out = jQuery.getJSON("../Olfaction/Onewt_"+ count +".json",function( data ) {
     console.log(count++);
     startOlf = data.olfaction_effects[0].start;
     duration = data.olfaction_effects[0].duration;
     play_olfaction(duration,data.olfaction_effects[0].fan_number);
   });
   if(playing == true){setTimeout(JSONfunc, 10000);}

   console.log("end of function");
}

var stopJSONfunc = function () {
 playing = false;
}

var pauseJSONfunc = function () {
  playing = !playing;
}

var play_olfaction = function(duration, fan) {
  var diffUseServletConf = "#" + fan + ",SCENT_" + fan + ",,0," + duration / 1000 + ",10,";


  jQuery.ajax({
    url: "http://192.168.1.19:4000/",
    type: 'GET',
    data: {conf: diffUseServletConf},
    //dataType: 'json',
    success: function (resData) {
      console.log("Success: " + resData);
    },
    error: function (xhr, testStatus, errorThrown) {
      console.log(errorThrown);
      console.log(JSON.stringify(xhr));
      console.log(xhr.responseText);
    }
  });
}



////////////////////////////////////////////////////////////////////////
//Haptic Feedback                                                     //
////////////////////////////////////////////////////////////////////////

var countH = 1;
var JSONfuncHaptic = function () {
  var  out = jQuery.getJSON("../Haptic/Hnewt_"+ countH +".json",function( data ) {
    bind_game_event(data.haptic_effects[0].description);
    countH++;
    console.log("haptic");
    console.log(data.haptic_effects[0].start);
    setTimeout(function () {
        send_game_event();
    }, data.haptic_effects[0].start);
  });
  if(playing == true){setTimeout(JSONfuncHaptic, 10000);}

}

var bind_game_event = function (effect){
  var url = "http://" + engineAddress + "/bind_game_event";
  var payload =
      {
        "game": "RIVAL",
        "event": "HAPTIC",
        "handlers": [
          {
            "device-type": "tactile",
            "zone": "one",
            "mode": "vibrate",
            "pattern": effect.pattern,
            "rate": effect.rate
          }
        ]
      }
  do_post(url, payload);
}


//from Longhao
var send_game_event = function (){
  var url = "http://" + engineAddress + "/game_event";
  var payload = {
    "game": "RIVAL",
    "event": "HAPTIC",
    "data": {
      "value": "10" //value is not used so it can be anything
    }
  };
  do_post(url, payload);
};

//from Longhao
var do_post = function(url, data){
  var http = new XMLHttpRequest();
  http.open("POST", url, true);
  http.setRequestHeader("Content-Type", "application/json");
  http.send(JSON.stringify(data));
};
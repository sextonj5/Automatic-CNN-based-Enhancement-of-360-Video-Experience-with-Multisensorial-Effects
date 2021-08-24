<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>

var getJSONFile = function () {
    var  out = jQuery.getJSON("../Onewt_01.json",function( data ) {
        return data;
    })
    return out;
}

getJSONFile();
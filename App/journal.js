String.prototype.isEmpty = function(){
  return (this.length === 0 || !this.trim());
};


var guestMessages = {
  title: [],
  msgs: [],

  getMessages: function(msg){
    this.title.push(value1 + "<br>");
    this.msgs.push("<br>"+ value);
  },

  printMessages: function(){
    guestMessages.getMessages();
    var showTitle = document.getElementById("titleoutput").innerHTML = this.title.join(" ");
    var showEntry = document.getElementById("entry").innerHTML = this.msgs.join(" ");
  }
};

//console.log(keepmsgs);

var getEntry = function(){
  value1 = document.getElementById("title").value;
  value = document.getElementById("content").value;
  return value1 + value;
};


var clearDiv = function(){
  document.getElementById("title").value = "";
  document.getElementById("content").value = "";
}

var isEmpty = function(entry){
  entry = getEntry();
  var output = document.getElementById("content").value;
  var output2 = document.getElementById("title").value;
  if ( output === '' || output2 === '' ){
    alert("Incomplete fields! Fill in all boxes");
  }
  else {
    guestMessages.printMessages();
  }
}

// updateEntry();

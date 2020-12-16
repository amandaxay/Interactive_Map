String.prototype.isEmpty = function(){
  return (this.length === 0 || !this.trim());
};


var guestMessages = {
  // entry = title + msgs
  entry: [],
  title: "",
  msgs: "",

  getMessages: function(msg){
    this.title = value1 + "<br>";
    this.msgs = "<h6 style='font-size:20px; padding-left:30px;'>" + value + "</h6>" + "<br>";
    this.entry.push(this.title + this.msgs);
  },

  printMessages: function(){
    guestMessages.getMessages();

    var showTitle = document.getElementById("titleoutput").innerHTML = this.title;
    var showEntry = document.getElementById("paragraph").innerHTML = this.msgs;

    var show = document.getElementById("entry").innerHTML = this.entry.join(" ");


    console.log(guestMessages.entry);
    console.log(guestMessages.title);
    console.log(guestMessages.msgs);
  },
};


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
  var output = document.getElementById("title").value;
  var output2 = document.getElementById("content").value;
  if ( output === '' || output2 === '' ){
    alert("Incomplete fields! Fill in all boxes");
  }
  else {
    guestMessages.printMessages();
  }
}

// updateEntry();

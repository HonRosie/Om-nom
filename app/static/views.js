function bindTaskEvents(){
  var tasks = document.querySelectorAll(".task");

  for(var i = 0; i<tasks.length; i++){
    tasks[i].addEventListener("keydown", function(e) {
      if (e.keyCode === 13){
        $.post('/todo/' + e.target.id.substring(4) + '/edit', {"editTask": e.target.value}, function(resp) {
          document.querySelector("#taskList").innerHTML = $(resp).get(0).innerHTML;
          bindTaskEvents();
        });
      }
    });
  }
}

bindTaskEvents();
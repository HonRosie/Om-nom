var replaceOccuring = false;

function bindTaskEvents(){
  var tasks = document.querySelectorAll(".task");

  for(var i = 0; i<tasks.length; i++){
    tasks[i].addEventListener("keydown", function(e) {
      if (e.keyCode === 13){
        $.post('/todo/' + e.target.id.substring(4) + '/edit',
               {"editTask": e.target.value, "createNew": true}, function(resp) {
          replaceTaskList(resp)
        });
      }
      else if (e.shiftKey && e.keyCode === 9){
        e.preventDefault()
        $.post('/todo/' + e.target.id.substring(4) + '/unSubTask',
               {"subTask": e.target.value}, function(resp){
          replaceTaskList(resp);
          document.getElementById(e.target.id).focus();
        });
      }
      else if (e.keyCode === 9){
        e.preventDefault();
        $.post('/todo/' + e.target.id.substring(4) + '/addSubTask',
               {"subTask": e.target.value}, function(resp){
          replaceTaskList(resp)
          document.getElementById(e.target.id).focus()
        });
      }
      else if (e.ctrlKey && e.keyCode == 68){
        $.post('/todo/' + e.target.id.substring(4) + '/toggleDone', function(resp){
          replaceTaskList(resp)
        });
      }
    });
    tasks[i].addEventListener("blur", function(e) {
      if (replaceOccuring) return;
      $.post('/todo/' + e.target.id.substring(4) + '/edit',
             {"editTask": e.target.value, "createNew": false}, function(resp) {
          replaceTaskList(resp)
      });
    });
  }
}

function replaceTaskList(resp){
  replaceOccuring = true;
  document.querySelector("#taskList").innerHTML = $(resp).get(0).innerHTML;
  bindTaskEvents();
  replaceOccuring = false;
}

bindTaskEvents();

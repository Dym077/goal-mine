const editButtons = document.getElementsByClassName("btn-edit");
const taskText = document.getElementById("id_body");
const taskForm = document.getElementById("taskForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/** The for loop enables editing of each unique task */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let taskId = e.target.getAttribute("task_id");
      let taskContent = document.getElementById(`task${taskId}`).innerText;
      taskText.value = taskContent;
      submitButton.innerText = "Update";
      taskForm.setAttribute("action", `edit_task/${taskId}`);
    });
  }

/** The for loop enables deletion of each unique task */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let taskId = e.target.getAttribute("task_id");
      deleteConfirm.href = `delete_task/${taskId}`;
      deleteModal.show();
    });
  }  

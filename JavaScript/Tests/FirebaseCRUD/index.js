import { saveTask, 
         getTasks, 
         onGetTask,
         deleteTask
        } from "./firebase.js";

const tasksContainer = document.getElementById("tasks-container");
const taskForm = document.getElementById("task-form");


window.addEventListener('DOMContentLoaded', async () => {
    //const querySnapshot = await getTasks();
    
    onGetTask((querySnapshot) => {
        let html = "";

        querySnapshot.forEach(doc => {
            const task = doc.data();
            html += `<div>
                        <h3>${task.title}</h3>
                        <p>${task.description}</p>
                     </div>
                     <button class="btn-delete" data-id="${doc.id}">Delete</button>
                    `; 
        });

        tasksContainer.innerHTML = html;

        const btnDelete = tasksContainer.querySelectorAll(".btn-delete");              

        btnDelete.forEach(btn => {
            btn.addEventListener('click', ({target :{dataset: {id}}}) => {
                deleteTask(id);
            });
        });
    });
})

taskForm.addEventListener('submit', (e) =>{
    e.preventDefault();

    const title = taskForm['task-title'];
    const description = taskForm['task-description'];

    saveTask(title.value, description.value);
    
    taskForm.reset();
})
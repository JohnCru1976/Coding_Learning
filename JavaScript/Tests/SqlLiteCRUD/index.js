import { saveTask, 
         getTasks, 
         onGetTask,
         deleteTask,
         getTask,
         updateTask
        } from "./sqlite.js";

const tasksContainer = document.getElementById("tasks-container");
const taskForm = document.getElementById("task-form");

let editStatus = false;
let id = '';

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
                     <button class="btn-edit" data-id="${doc.id}">Edit</button>
                    `; 
        });

        tasksContainer.innerHTML = html;

        const btnDelete = tasksContainer.querySelectorAll(".btn-delete"); 
        const btnEdit = tasksContainer.querySelectorAll(".btn-edit");             

        btnDelete.forEach(btn => {
            btn.addEventListener('click', ({target :{dataset: {id}}}) => {
                deleteTask(id);
            });
        });

        btnEdit.forEach(btn => {
            btn.addEventListener('click', async ({target: {dataset}}) => {
                editStatus = true;
                const doc = await getTask(dataset.id);
                const task = doc.data();
                taskForm["task-title"].value = task.title;
                taskForm["task-description"].value = task.description;
                id = dataset.id;
                taskForm['btn-task-save'].innerText = "Update";                
            })
        });
    });
})

taskForm.addEventListener('submit', (e) =>{
    e.preventDefault();

    const title = taskForm['task-title'];
    const description = taskForm['task-description'];

    if (editStatus){
        updateTask(id,{'title': title.value, 'description': description.value});
        editStatus = false;
        taskForm['btn-task-save'].innerText = "Save";
    }else{
        saveTask(title.value, description.value);
    }
    
    taskForm.reset();
})
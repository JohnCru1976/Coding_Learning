// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { getFirestore,
         onSnapshot, 
         collection,
         getDocs,
         doc, 
         addDoc,      // Create        
         getDoc,      // Read
         updateDoc,   // Update
         deleteDoc    // Delete    
        } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-firestore.js"

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyC0J-fp-gSXN-sgj-MVHDNWMXJf1JCveRU",
  authDomain: "todo-b8bdc.firebaseapp.com",
  projectId: "todo-b8bdc",
  storageBucket: "todo-b8bdc.appspot.com",
  messagingSenderId: "444889236167",
  appId: "1:444889236167:web:83a12c6d0c9ec3e48474e2"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore();

// CRUD FUNCTIONS
export const getTasks = () => 
  getDocs(collection(db,"tasks"));

export const onGetTask = (callback) => 
  onSnapshot(collection(db,"tasks"), callback);

export const saveTask = (title, description) => 
  addDoc(collection(db, 'tasks'), {title: title, description: description});

export const deleteTask = id => 
  deleteDoc(doc(db, 'tasks', id));

export const getTask = id => 
  getDoc(doc(db, 'tasks', id));

export const updateTask = (id, newFields) => 
  updateDoc(doc(db,'tasks', id), newFields);

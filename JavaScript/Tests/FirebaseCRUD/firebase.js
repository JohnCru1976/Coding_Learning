// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
import { getFirestore, 
         collection, 
         addDoc,
         getDocs,
         deleteDoc,
         onSnapshot,
         doc 
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
export const saveTask = (title, description) => {
    addDoc(collection(db, 'tasks'), {title: title, description: description});
};

export const getTasks = () => getDocs(collection(db,"tasks"));

export const onGetTask = (callback) => onSnapshot(collection(db,"tasks"), callback);

export const deleteTask = id => deleteDoc(doc(db, 'tasks', id));

// Import the functions you need from the SDKs you need
import { initializeApp } from "../firebase/app";
import { getAuth } from "../firebase/auth";
import { getFirestore } from "../firebase/firestore";
import { getStorage } from "../firebase/storage";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

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
// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);
// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(app);
// Initialize Cloud Storage and get a reference to the service
const storage = getStorage(app);
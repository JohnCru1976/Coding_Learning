
// Initialize database
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

''' This is an exercise to learn the basics of firebase with Python
Part of the code in this file has been obtained using CHAT-GPT'''
import os
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from random import randint

# Set the working directory on the file directory
file_directory = os.path.dirname(__file__)
os.chdir(file_directory)

# Prepare the credentials obtained from web
credent = credentials.Certificate("todo-b8bdc-firebase-adminsdk-jryak-dcaab7f0ff.json")
# Se conecta la base de datos
firebase_admin.initialize_app(credent)
# Se crea un interfaz para conectar con la base de datos
db = firestore.client()

# Crear una COLLECTION - (Una base de datos relacional)
coleccion = db.collection("test_collection")

#######################################
# CRUD OPERATIONS
#######################################

def create_document(coleccion_obj, document_id, data):
    '''Create a new document with a specific ID'''
    doc_ref = coleccion_obj.document(document_id)
    doc_ref.set(data)

def read_document(coleccion_obj, document_id):
    '''Read a document by its ID'''
    doc_ref = coleccion_obj.document(document_id)
    document = doc_ref.get()
    if document.exists:
        return document.to_dict()
    else:
        return None

def update_document(coleccion_obj, document_id, data):
    '''Update a document by its ID'''
    doc_ref = coleccion_obj.document(document_id)
    doc_ref.update(data)


def delete_document(coleccion_obj, document_id):
    '''Delete a document by its ID'''
    doc_ref = coleccion_obj.document(document_id)
    doc_ref.delete()

#############################################
# QUERIES  EJEMPLOS
#############################################

def query_all_documents(coleccion_obj):
    '''Consulta para recuperar todos los documentos en una colección'''
    documents = coleccion_obj.stream()

    for document in documents:
        print(f"ID: {document.id}")
        print(f"Datos: {document.to_dict()}")


def query_with_condition(coleccion_obj):
    '''Consulta con una condición (por ejemplo, obtener usuarios mayores de 30 años)'''
    query = coleccion_obj.stream()

    filtered_docs = filter(lambda doc: doc.to_dict().get("age") > 30, query)

    for document in filtered_docs:
        print(f"ID: {document.id}")
        print(f"Datos: {document.to_dict()}")


def query_with_order(coleccion_obj):
    '''Consulta con ordenamiento (por ejemplo, ordenar por nombre de usuario)'''
    query = coleccion_obj.order_by("age").stream()

    for document in query:
        print(f"ID: {document.id}")
        print(f"Datos: {document.to_dict()}")


#############################################
###############  PRUEBAS ####################
#############################################

# Example data to use
user_data = {
        "name": "Usuario 1",
        "email": "usuario1@example.com",
        "age": 25
        }

# Create a new document
create_document(coleccion, "user1", user_data)

for n in range(2, 20):
    user_data = {
        "name": f"Usuario {n}",
        "email": f"usuario{n}@example.com",
        "age": randint(15,60)
        }
    # Create a new document
    create_document(coleccion, f"user{n}", user_data)

# Read the document
result = read_document(coleccion, "user1")
print("Read Document:")
print(result)

# Update the document
updated_data = {"age": 31}
update_document(coleccion, "user1", updated_data)

# Read the updated document
result = read_document(coleccion, "user1")
print("Read Updated Document:")
print(result)

# Delete the document
delete_document(coleccion, "user1")
print("Document deleted.")

# Attempt to read the deleted document
result = read_document(coleccion, "user1")
print("Read Deleted Document:")
print(result)


# Create a new document
create_document(coleccion, "user1", user_data)

# Create a new document
create_document(coleccion, "user1", user_data)

query_all_documents(coleccion)
print("*" * 20)
print("*" * 20)
print("*" * 20)
query_with_condition(coleccion)
print("*" * 20)
print("*" * 20)
print("*" * 20)
query_with_order(coleccion)

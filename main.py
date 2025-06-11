from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hellow welcom to my fastapi deploymentr in an AWS EC2 instance'}

# lets create a fastapi that has the returns the a students profile when called

students = {
    1 : {
        'name': 'Obi Peters',
        'age': 14,
        'year': 'year 7'
    },
    2 : {
        'name': 'Sharon Ojo',
        'age': 15,
        'year': 'year 8'
    },
    3 : {
        'name': 'Kalu Esther',
        'age': 12,
        'year': 'year 5'
    },
    4 : {
        'name': 'Mercy Grace',
        'age': 10,
        'year': 'year 4'
    },
    5 : {
        'name': 'Obi Paul',
        'age': 14,
        'year': 'year 7'
    },
}

@app.get('/student_id/{student_id}')
async def get_student_profile(student_id : int, name :str ):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
        else:
            return {'name': 'student not in database'}
        

@app.get('items/{items_id}')
async def items(items_id):
    return {'item_id': items_id}
from fastapi import APIRouter, Query, Path
from fastapi.responses import JSONResponse

from app.db import DB_CONNECTION
from app.db.instance import Instance

router1 = APIRouter()


@router1.post("/add-record", status_code=201)
def add_record(
    column1: str = Query(None, description="column1 - string"), 
    column2: int = Query(None, description="column2 - int")):
    """
    Add record to test_table
    """

    with Instance(**DB_CONNECTION) as instance:
        instance.execute_query(f"INSERT INTO test_table (column1, column2) VALUES ('{column1}', {column2});")
        id = instance.read_query('SELECT max(id) FROM test_table;')[0][0]

        return {
            'status': f'Record column1: {column1}, column2: {column2} added with ID:{id}'
        }    

    return {'error': instance.exc}


@router1.get("/get-record/{id}", status_code=200)
def get_record(id: int = Path(description="Record ID")):
    """
    Get record to test_table by ID 
    """

    with Instance(**DB_CONNECTION) as instance:
        record = instance.read_query(f'SELECT column1, column2 FROM test_table WHERE id={id};')

        response, code = f'Record ID: {id} not found', 404
        if record:
            response, code = f'Record ID: {id}, column1: {record[0][0]}, column2: {record[0][1]}', 200
        return JSONResponse(content={'status': response}, status_code=code)

    return {'error': instance.exc}
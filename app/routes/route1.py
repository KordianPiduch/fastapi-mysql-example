from fastapi import APIRouter, Query, Path

router1 = APIRouter()


@router1.get("/test")
def endpoint():
    return {'status': "response from endpoint in route1"}


@router1.get("/user/{user_name}")
def welcome(user_name: str = Path(description="First Name"), id_number: int = Query(None, description="User id number")):
    """
    print welcome message with id number 
    """
    return {'status': f"Welcome {user_name} - {id_number}"}
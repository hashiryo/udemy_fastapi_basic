from fastapi import APIRouter
import schemas.contact as contact_schema
from datetime import datetime
router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.Contact])
async def get_contact_all():
 dummy_data = datetime.now()
 return [contact_schema.Contact(id=1,
                                name="山田",
                                email="test@test.com",
                                url="http://test.com",
                                gender=1, 
                                message="Hello World",
                                is_enabled=False, 
                                created_at=dummy_data)]

@router.post("/contacts", response_model= contact_schema.Contact)
async def create_contact(body: contact_schema.Contact):
 return contact_schema.Contact(**body.model_dump())
 

@router.get("/contacts/{id}")
async def get_contact():
 pass

@router.put("/contacts/{id}")
async def update_contact():
 pass

@router.delete("/contacts/{id}")
async def delete_contact():
 pass
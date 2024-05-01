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
 

@router.get("/contacts/{id}", response_model=contact_schema.Contact)
async def get_contact(id: int):
 return contact_schema.Contact(id)

@router.put("/contacts/{id}", response_model=contact_schema.Contact)
async def update_contact(id: int, body: contact_schema.Contact):
 return contact_schema.Contact(**body.model_dump())

@router.delete("/contacts/{id}", response_model=contact_schema.Contact)
async def delete_contact(id: int):
 return
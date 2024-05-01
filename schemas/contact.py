from pydantic import BaseModel, Field
from datetime import datetime

class Contact(BaseModel):
 id: int
 name: str
 email: str
 url: str
 gender: int
 message: str
 is_enabled: bool
 created_at: datetime
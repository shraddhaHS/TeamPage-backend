from pydantic import BaseModel
from typing import Optional

class TeamMemberCreate(BaseModel):
    name: str
    role: str
    bio: Optional[str] = None
    funFact: Optional[str] = None
    linkedInUrl: Optional[str] = None
    xUrl: Optional[str] = None


class TeamMemberUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    bio: Optional[str] = None
    funFact: Optional[str] = None
    linkedInUrl: Optional[str] = None
    xUrl: Optional[str] = None
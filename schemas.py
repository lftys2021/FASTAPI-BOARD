from pydantic import BaseModel, Field
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str
    # author: str

class PostUpdate(BaseModel):
    title: str
    content: str
    # author: str

class UserInfo(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class AuthorResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class ReplyResponse(BaseModel):
    id: int
    content: str

    author: AuthorResponse

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ReplyCreate(BaseModel):
    content: str

class ReplyDetailResponse(ReplyResponse):
    replies: list[ReplyResponse]

class CommentResponse(BaseModel):
    id: int
    content: str
    owner_id: int
    author: AuthorResponse
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CommentDetailResponse(CommentResponse):
    replies: list["ReplyResponse"] = []
    likes_count: int = 0



class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    author: AuthorResponse      # ← 이걸 기대하고 있음

    created_at: datetime
    updated_at: datetime

    likes_count: int

    class Config:
        from_attributes = True

class PostDetailResponse(PostResponse):
    comments: list[CommentResponse]

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: str
    email: str
    password: str

class PostWithLikes(BaseModel):
    id: int
    title: str
    content: str

    likes_count: int

    class Config:
        from_attributes = True

class CommentCreate(BaseModel):
    content: str

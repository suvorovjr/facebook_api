from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class DataModel(BaseModel):
    created_time: datetime
    message: str
    id: str


class CursorModel(BaseModel):
    before: str
    after: str


class PagingModel(BaseModel):
    cursors: CursorModel
    next: Optional[str] = Field(default=None)


class ResponseAPIModel(BaseModel):
    data: List[DataModel]
    paging: PagingModel


class PagesDataModel(BaseModel):
    access_token: str
    category: str
    name: str
    id: str


class PagesResponseModel(BaseModel):
    data: List[PagesDataModel]
    paging: PagingModel

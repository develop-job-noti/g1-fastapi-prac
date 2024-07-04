"""Response 객체 분리 이유
    다양한 유스케이스가 있기 떄문에
    미리 Response 객체를 분리 해놓게 되면
    유연하게 코드 변경을 할 수 있다.

    Django의 Serializer랑 비슷한 느낌인 것 같다.
"""

from typing import List
from pydantic import BaseModel


class ToDoSchema(BaseModel):
    id: int
    contents: str
    is_done: bool

    class Config:
        orm_mode = True


class TodoListSchema(BaseModel):
    todos: List[ToDoSchema]

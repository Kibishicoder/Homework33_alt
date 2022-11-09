from dataclasses import field
from typing import List, Optional

# from marshmallow_dataclass import dataclass
# from marshmallow import EXCLUDE
from marshmallow import EXCLUDE
from marshmallow_dataclass import dataclass


@dataclass
class MessageFrom:
    id: int
    first_name: Optional[str] = field(default=None)
    last_name: Optional[str] = field(default=None)
    username: Optional[str] = field(default=None)

    class Meta:
        unknown = EXCLUDE


@dataclass
class Chat:
    id: int
    type: str
    first_name: Optional[str] = field(default=None)
    last_name: Optional[str] = field(default=None)
    username: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)

    class Meta:
        unknown = EXCLUDE


@dataclass
class Message:
    message_id: int
    chat: Chat
    # override usage of keyword "from" - add underscore and metadata to map to data key
    from_: Optional[MessageFrom] = field(metadata=dict(data_key='from'), default=None)
    text: Optional[str] = field(default=None)

    class Meta:
        unknown = EXCLUDE


@dataclass
class UpdateObj:
    update_id: int
    message: Optional[Message] = field(default=None)

    class Meta:
        unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateObj]

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message

    class Meta:
        unknown = EXCLUDE

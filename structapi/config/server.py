"""
Example of the constant configures
"""

from pydantic import BaseModel, IPvAnyAddress


class Server(BaseModel):
    id: int
    ip: IPvAnyAddress  # IPv4 address protocol like "192.168.0.1"
    port: int
    site_code: str

    class Config:
        env_file = ".env"


class DBMS(BaseModel):
    host: str
    port: int
    db: str
    userid: str
    passwd: str
    duration: int = 15  # reconnect duration per seconds


class MySQL(DBMS):
    pass


class Redis(DBMS):
    subscribe: str

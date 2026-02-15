"""Agent Session Manager - Session management for agent interactions."""

from typing import Dict, Any
from dataclasses import dataclass, field
from datetime import datetime
import uuid

class AgentSessionManager:
    def __init__(self):
        self.sessions: Dict[str, Dict] = {}
    
    def create_session(self, agent_id: str) -> str:
        sid = str(uuid.uuid4())
        self.sessions[sid] = {"agent_id": agent_id, "created": datetime.now(), "data": {}}
        return sid
    
    def get_session(self, sid: str) -> Dict:
        return self.sessions.get(sid)
    
    def update_session(self, sid: str, data: Dict) -> bool:
        if sid in self.sessions:
            self.sessions[sid]["data"].update(data)
            return True
        return False
    
    def delete_session(self, sid: str) -> bool:
        return self.sessions.pop(sid, None) is not None

__all__ = ["AgentSessionManager"]

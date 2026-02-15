#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import AgentSessionManager
def main():
    print("Agent Session Manager Demo")
    m = AgentSessionManager()
    sid = m.create_session("a1")
    m.update_session(sid, {"key": "value"})
    print(f"Session: {m.get_session(sid) is not None}")
    print("Done!")
if __name__ == "__main__": main()

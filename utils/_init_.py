import json
import os
from datetime import datetime, timedelta

# In-memory session storage (for development)
# For production, consider using Redis or a database
sessions = {}

class SessionExpired(Exception):
    pass

def get_session(session_id, create_if_missing=True):
    """Retrieve or create a session"""
    if session_id not in sessions:
        if not create_if_missing:
            return None
        sessions[session_id] = {
            'created_at': datetime.now(),
            'last_accessed': datetime.now(),
            'data': {
                'phone_number': session_id  # Using phone number as session ID
            }
        }
    else:
        # Check if session expired (30 minutes inactivity)
        last_access = sessions[session_id]['last_accessed']
        if datetime.now() - last_access > timedelta(minutes=30):
            del sessions[session_id]
            raise SessionExpired("Session expired due to inactivity")
        
        # Update last accessed time
        sessions[session_id]['last_accessed'] = datetime.now()
    
    return sessions[session_id]['data']

def update_session(session_id, key, value):
    """Update a session value"""
    session = get_session(session_id)
    session[key] = value
    sessions[session_id]['last_accessed'] = datetime.now()

def clear_session(session_id):
    """Clear a session"""
    if session_id in sessions:
        del sessions[session_id]

def save_sessions_to_file(filename="sessions_backup.json"):
    """Backup sessions to file (for persistence)"""
    with open(filename, 'w') as f:
        json.dump(sessions, f, default=str)

def load_sessions_from_file(filename="sessions_backup.json"):
    """Load sessions from file"""
    global sessions
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            sessions = json.load(f)
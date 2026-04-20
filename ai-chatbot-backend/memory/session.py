SESSIONS = {}

def get_session(sid):
    if sid not in SESSIONS:
        SESSIONS[sid] = {'history': [], 'plan': None}
    return SESSIONS[sid]

def update_session(sid, data):
    SESSIONS[sid] = data
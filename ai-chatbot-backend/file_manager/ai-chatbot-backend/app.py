from flask import Flask, request, jsonify
from memory.session import get_session, update_session
from ai.planner import plan_project
from ai.generator import generate_project
from file_manager.writer import write_project_files
import uuid

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "message is required"}), 400

    session_id = data.get("session_id") or str(uuid.uuid4())
    session = get_session(session_id)

    session["history"].append({"role": "user", "content": data["message"]})

    if not session.get("plan"):
        plan_response = plan_project(session["history"])
        if plan_response["type"] == "question":
            session["history"].append({"role": "assistant", "content": plan_response["content"]})
            update_session(session_id, session)
            return jsonify({"session_id": session_id, "reply": plan_response["content"]})
        session["plan"] = plan_response["content"]

    code = generate_project(session["plan"])
    path = write_project_files(session_id, code)

    update_session(session_id, session)
    return jsonify({"session_id": session_id, "reply": "✅ Website created", "path": path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
    
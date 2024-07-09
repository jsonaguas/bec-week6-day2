from flask import Flask, request, jsonify
import mysql.connector
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

db_config = {
	'user': 'root',
	'host': 'localhost',
	'database': 'workout'
}
def get_db_connection():
	conn = mysql.connector.connect(**db_config)
	return conn


class MemberSchema(ma.Schema):
	class Meta:
		fields = ('id', 'name', 'email', 'phone')

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

class WorkoutSessionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'member_id', 'date', 'time', 'duration', 'description')

session_schema = WorkoutSessionSchema()
sessions_schema = WorkoutSessionSchema(many=True)


@app.route('/') # default landing page
def home():
    return "Hello, Flask!"

@app.route('/members', methods=['POST'])
def add_member():
	data = request.get_json()

	return jsonify({'message': 'Member added successfully'}), 201

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
    member = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(member_schema.dump(member)), 200

@app.route('/members', methods=['GET'])
def get_all_members():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members")
    members = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(members_schema.dump(members)), 200

@app.route('/members/<int:member_id>/workout_sessions', methods=['GET'])
def get_member_sessions(member_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
    member = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(member_schema.dump(member)), 200

@app.route('/workout_sessions/<int:id>', methods=['GET'])
def get_session(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM WorkoutSessions WHERE id = %s", (id,))
    session = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(session_schema.dump(session)), 200

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
    member = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(member_schema.dump(member)), 200

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
    member = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(member_schema.dump(member)), 200


@app.route('/workout_sessions', methods=['POST'])
def schedule_session():
	conn = get_db_connection()
	cursor = conn.cursor(dictionary=True)
	cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
	member = cursor.fetchone()
	cursor.close()
	conn.close()
	return jsonify(member_schema.dump(member)), 200

@app.route('/workout_sessions/<int:id>', methods=['PUT'])
def update_session(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
    member = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(member_schema.dump(member)), 200

@app.route('/workout_sessions/<int:id>', methods=['DELETE'])
def delete_session(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
    member = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(member_schema.dump(member)), 200

@app.route('/workout_sessions', methods=['GET'])
def get_all_sessions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM WorkoutSessions")
    sessions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(sessions_schema.dump(sessions)), 200





if __name__ == '__main__':
	app.run(debug=True)
	
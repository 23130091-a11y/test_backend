from flask import Flask, jsonify

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Tạo route đơn giản
@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Xin chào từ Flask API!"})

# Chạy server
if __name__ == '__main__':
    app.run(debug=True)

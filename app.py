from flask import Flask, send_from_directory, abort, render_template
import os

app = Flask(__name__)

# 设置文件目录
FILE_DIRECTORY = os.path.join(os.path.dirname(__file__), 'files')

@app.route('/')
def index():
    return render_template('index.html', message="Put here the message that you want to send")

@app.route('/download/clash', methods=['GET'])
def download_file():
    try:
        # 安全校验：避免目录穿越攻击
        # if '..' in filename or filename.startswith('/'):
        #     abort(400, description="Invalid filename")

        return send_from_directory(FILE_DIRECTORY, "Switch.eSIM2.0.7.apk", as_attachment=True)
    except FileNotFoundError:
        abort(404, description="File not found")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)

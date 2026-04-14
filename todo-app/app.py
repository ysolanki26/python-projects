from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({"text": task, "done": False})
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

@app.route('/complete/<int:index>')
def complete(index):
    tasks[index]["done"] = not tasks[index]["done"]
    return redirect('/')

@app.route('/clear')
def clear():
    tasks.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory content storage (just for demo)
contents = []

@app.route('/')
def index():
    return render_template('index.html', contents=contents)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        if title:
            contents.append(f"{title}: {content}")
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    if item_id < 0 or item_id >= len(contents):
        return "Item not found", 404
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        contents[item_id] = f"{title}: {content}"
        return redirect(url_for('index'))
    return render_template('edit.html', content=contents[item_id], item_id=item_id)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    if item_id < 0 or item_id >= len(contents):
        return "Item not found", 404
    contents.pop(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

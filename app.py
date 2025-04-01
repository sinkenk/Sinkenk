from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return render_template('intex.html')

# Обработка sitemap.xml
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.root_path, 'sitemap.xml', mimetype='application/xml')

# Обработка favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

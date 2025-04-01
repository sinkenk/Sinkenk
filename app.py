from flask import Flask, render_template, send_from_directory # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('intex.html')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')  # Отдача файла sitemap.xml

if __name__ == '__main__':
    app.run(debug=True)

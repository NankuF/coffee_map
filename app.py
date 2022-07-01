from flask import Flask


def read_map():
    with open('map.html', 'rb') as file:
        return file.read()


def run_site():
    app = Flask(__name__)
    app.add_url_rule('/', 'moscow_cafe', read_map)
    app.run('0.0.0.0')


if __name__ == '__main__':
    run_site()

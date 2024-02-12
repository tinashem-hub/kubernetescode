from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = "My name is Prince l love DevOps😎!!"
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                text-align: center;
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #007bff;
            }
            p {
                color: #343a40;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My Fancy Flask App!</h1>
            <p>{{ message }}</p>
        </div>
    </body>
    </html>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)


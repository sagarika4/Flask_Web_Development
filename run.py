from flaskblog import create_app # imports from init.py from flaskblog package
app=create_app('''config can be passed here''')

if __name__ == "__main__":
    app.run(debug=True, port=8000)

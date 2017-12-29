from application.Application import Application

if __name__ == '__main__':
    app = Application()
    print(app.state)
    app.state = 'Moved'
    print(app.state)
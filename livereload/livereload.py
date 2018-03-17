from flask.ext.script import Manager
app.config['DEBUG']=True
manager = Manager(app)                              # app 管理
@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')			    # 监视project下的所有文件和目录的变化，可以自定义其他的监视目录
    live_server.serve(open_url=True)

if __name__ == '__main__': 			    # 以flask管理的方式运行，使用```python app.py runserver ```就可以运行flask了
    manager.run()

# This file is also used on the server, in PythonAnywhere, read from
# the WSGI-config file /var/www/sympbio_pythonanywhere_com_wsgi.py
# ("from website.my_asreview_flask_app import app as application")


from .app import create_app
# from .admin import add_admin_views

app = create_app()
# add_admin_views(app)


if __name__ == '__main__':
    app.run(debug=True)

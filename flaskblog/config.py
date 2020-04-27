import os

class Config:
	SECRET_KEY='033dff7d4837f5d287dc53aad9946586'
	SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
	MAIL_SERVER='smtp.googlemail.com'
	MAIL_PORT=587
	MAIL_USE_TLS=True
	MAIL_USERNAME=os.environ.get('EMAIL_USER')
	MAIL_PASSWORD=os.environ.get('EMAIL_PASS')

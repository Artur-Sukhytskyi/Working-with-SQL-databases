import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):

	__tablename__ = 'user'

	id = sa.Column(sa.Integer, primary_key = True)

	first_name = sa.Column(sa.Text)

	last_name = sa.Column(sa.Text)

	gender = sa.Column(sa.Text)

	email = sa.Column(sa.Text)

	birthdate = sa.Column(sa.Text)

	height = sa.Column(sa.Float)

def connect_db():
	
	engine = sa.create_engine(DB_PATH)

	Base.metadata.create_all(engine)

	session = sessionmaker(engine)

	return session()

def request_data():
	
	print("Привет! Мы запишем твои данные!")

	first_name = input("Введите своё имя: ")

	last_name = input("А теперь фамилию: ")

	gender = input("Какого вы пола? (Варианты: Male/Female) ")

	email = input("Нам ещё понадобится ваш адрес электронной почты: ")

	birthdate = input("Введите, вашу дату рождения в формате ГГГГ-ММ-ДД. Например, 2020-02-02: ")

	height = input("Какой у вас рост в метрах? (Для разделения целой и десятичной части используй точку) ")

	user = User(

		first_name = first_name,
		last_name = last_name,
		gender = gender,
		email = email,
		birthdate = birthdate,
		height = height
	)
	return user

def main():

	session = connect_db()

	user = request_data()

	session.add(user)

	session.commit()

	print("Ваши данные сохранены в базе данных.")


if __name__ == "__main__":
	main()
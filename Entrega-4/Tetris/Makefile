create-env:
	cd server && echo "DB_USER=tetris-admin\nDB_PASSWORD=vI4el5wqFtvHbTnV" > .env

docker-build:
	sudo docker-compose build

docker-up:
	sudo docker-compose up

run: create-env docker-build docker-up

create-env:
	cd tetris-puzzle/server && echo "DB_USER=tetris-admin\nDB_PASSWORD=vI4el5wqFtvHbTnV" > .env

docker-build:
	cd tetris-puzzle && sudo docker-compose build

docker-up:
	cd tetris-puzzle && sudo docker-compose up

run: create-env docker-build docker-up


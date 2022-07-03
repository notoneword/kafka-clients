up:
	docker compose up -d

down:
	docker compose down

consume:
	docker exec kafka-consumer python kafka_consumer.py

sh:
	docker exec kafka-consumer 
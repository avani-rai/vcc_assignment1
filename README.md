Microservice Application with RabbitMQ

This project sets up a message queue architecture using RabbitMQ on three virtual machines (VMs).

------------------------------------------------------
1. Create Three Virtual Machines
------------------------------------------------------
- VM1: RabbitMQ Server
- VM2: Message Producer
- VM3: Message Consumer

Ensure all VMs are in a private NAT-enabled network for internal communication.

------------------------------------------------------
2. Install RabbitMQ on VM1
------------------------------------------------------
Update the system and install RabbitMQ:
sudo apt update && sudo apt install -y rabbitmq-server

Enable and start RabbitMQ:
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server

Check if RabbitMQ is running:
sudo systemctl status rabbitmq-server

------------------------------------------------------
3. Install Python Dependencies on VM2 and VM3
------------------------------------------------------
On both VM2 and VM3, install Python and required dependencies:
sudo apt update && sudo apt install -y python3 python3-pip
pip3 install pika

------------------------------------------------------
4. Run the Microservices
------------------------------------------------------
Start the Producer (VM2):
python3 avani_p.py

Start the Consumer (VM3):
python3 Avani_r.py

Once running, the producer will send messages to the RabbitMQ server (VM1), and the consumer will receive and process them.

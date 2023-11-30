from locust import HttpUser, task, between
import os

DNS_NAME = os.getenv("DNS_NAME")
if not DNS_NAME.startswith("http"):
    DNS_NAME = f"http://{DNS_NAME}"

class user(HttpUser):

    host = DNS_NAME
    wait_time = between(1, 3)

    @task(1)
    def get_users(self):
        self.client.get("/")
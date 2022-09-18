# nginx_multiserver_upstream

example to server and load balance the same service from multiple servers using nginx only
so in case one of the services crashes the application will stay up


# USAGE
```bash
sudo docker-compose build
sudo docker-compose up
```

then refer to

```
http://{YOUR_IP/DOMAIN}
```

do f5 a multiple times to see nginx load balancing between the apps


# Memory Store

- Fully managed Inmemory database
- sub-millisecond data access
- Two engine supported
  - Redis
  - Memcached
- Only Internal IP
- Highly available with 99.9% SLA
- Import/Export data from Cloud Storage to memory store

### Connect with redis from compute vm
```bash
$ sudo apt install redis-tools
$ redis-cli -h 10.120.117.27 # internal ip of redis instance 
10.120.117.27:6379> ping
PONG
10.120.117.27:6379> set key value
OK
10.120.117.27:6379> get key
"value"
```

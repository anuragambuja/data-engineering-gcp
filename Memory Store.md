# Memory Store

- Fully managed Inmemory database
- sub-millisecond data access
- Two engine supported
  - Redis
    - Strings, Lists, Sets, Sorted Sets, Hashes, Bitmaps (based on Strings), HyperLogLogs (based on Strings, approx. number of distinct elements in list)
  - Memcached
    - Memcached is key-value store eg. {A_cnt: 10, B_cnt: 20, C_cnt: 24}
    - Useful for large caches
    - High availability clusters
- Only Internal IP
- Highly available with 99.9% SLA
- Import/Export data from Cloud Storage to memory store

### Differences with Open Source Redis
- Persisting to Disk
  - Available in OS version
    - point in time snapshots (RDB)
    - Logs of write Operations (AOF)
  - Not available in Cloud Memorystore
- Most parameters set and can't be changed in cloud memorystore
- Some Redis commands are blocked
- Standard Tier does not allow reading from replica 

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




# Python-Etcd Client

The Project Library is based on [kragniz/python-etcd3](https://github.com/kragniz/python-etcd3)

Some `Features`:
 - Multi-Server Failover Supports
 - Model Design
 - Easy Extension

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from pyetcd-client import client
client = EtcdClient(ServerList=("127.0.0.1:2379",),TLS=False)
```

## Model Framework
```bash
pythonetcd-client
 |- EtcdClient
 |- model
   |- Node
   |- Directory
```
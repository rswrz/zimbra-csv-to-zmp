# Intro
Create a `zmp` file from `csv` (Zimbra export) to bulk create users with random passwords with Zimbras `zmprov` tool.

- [Zimbra Bulk Provisioning](https://wiki.zimbra.com/wiki/Bulk_Provisioning)

# Create `zmp`

## Native Python
```
python3 ./create_zmp.py > commands.zmp
```

## Docker Container
```
docker run --rm -v $PWD:/app -w /app python:3 python create_zmp.py > commands.zmp
```

# Run `zmprov`
```
zmprov -f commands.zmp
```

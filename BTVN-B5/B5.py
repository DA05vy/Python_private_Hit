import pprint
docker_compose = {
    "version" : '3.8',
    "services" : 'app',
    "image" : 'python:3.10-slim',
    "command" : 'python app.py',
    "volumes" : './app:/app',
    "restart" : 'always',
    "ports" : '5000:5000',
    "depends_on" : "db"
}
def pri(): 
    pprint.pprint(docker_compose)
    print()

print("Ban đầu ")
pri()

docker_compose["version"] = '3.10'
print("Sau khi sửa version: ")
pri()


print("Giá trị của image: ", docker_compose["image"])
print()

docker_compose["enviroment"] = 'PYTHONUNBUFFERD = 1'
print("Sau khi thêm: ")
pri()

if 'volumes' in docker_compose:
    print(" 'volumes' có trong docker_compose " )
else:
    print(" Không có 'volumes' trong docker_compose ")
print()

del docker_compose["depends_on"]
pri()

print("Số lượng key: ", len(docker_compose))
print()

my_list = [ value for value in docker_compose.values()]
print(my_list)
print()

if 'always' in docker_compose.values():
    print("Giá trị 'always' có trong dictionary.")
else:
    print("Giá trị 'always' không có trong dictionary.")
print()

print("Nhập 1 cặp k-v mới")
key = input("Nhap key: ")
val = input("Nhap value: ")
docker_compose[key] = val
pri()





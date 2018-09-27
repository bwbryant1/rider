import ipaddress
test_net = type(ipaddress.ip_network('1.1.1.1/32'))

subnet1 = ipaddress.ip_network('10.0.0.0/24')

def explode_ip_list(ipadr):
    if type(ipadr) != test_net:
        return []
    working = []
    for _a in ipadr:
        working.append(_a.exploded)
    return working

def to_dict(name,_list):
    working = {}
    working[name] = _list
    return working

def save(name,data,file_out):
    with open(file_out + ".py",'w') as file:
        file.write(str(name) + " = { ")
        for k in sorted (data.keys()):
            file.write("'%s':%s, " % (k, data[k]))
        file.write("}")

def main():
    sub = explode_ip_list(subnet1)
    subdict = to_dict('private_subnet_range',sub)
    save("test_name",subdict,"out")
    from out import test_name
    print('10.0.0.10' in test_name['private_subnet_range'])

main()

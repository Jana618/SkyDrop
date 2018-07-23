
def calc_crc(sum, key, data):
    for i in range(0, 8):
        if ((data & 0x01)^(sum & 0x01)):
            sum = (sum >> 1) % 0x100 
            sum = (sum ^ key) % 0x100
        else:
            sum = (sum >> 1) % 0x100
        data = (data >> 1) % 0x100
        print sum, data
    return sum
            

#in_data = [0x0A, 0x02, 0x62, 0x69, 0x6E, 0x70, 0x72, 0x6e, 0x62, 0x65, 0x08]
#in_data = [0x0A, 0x02, 0x62, 0x69, 0x6F, 0x70, 0x72, 0x6F, 0x62, 0x65, 0x44] #0x17
in_data = [0x06] + map(ord, "bean2") + [0]


key = 0xD5
crc = 0x00
for c in in_data:
    print "%02X" % c
    crc = calc_crc(crc, key, c)
    print "crc -> %02X %3d" % (crc, crc)
    
print chr(60)

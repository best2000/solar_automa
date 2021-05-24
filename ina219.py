import smbus, subprocess, stat_logger, time
from gpiozero import InputDevice, OutputDevice

#relay is ACTIVE LOW
p6 = OutputDevice(6, active_high=False)
####

i2c_ch = 1

i2c_address = 0x40

reg_config = 0x00
reg_busv = 0x02
reg_pwr = 0x03

lsb = float(4.0/1000)

bus = smbus.SMBus(i2c_ch)

#set reg_config
val = bus.read_i2c_block_data(i2c_address, reg_config, 2)
val[0] = 0b00111111
val[1] = 0b10011110
bus.write_i2c_block_data(i2c_address, reg_config, val)

def read_busv():
    while True:
        try:
            #read NC
            p6.off()
            time.sleep(1)
            while True:
                val = bus.read_i2c_block_data(i2c_address, reg_busv, 2) #check CVRF
                pwr = bus.read_i2c_block_data(i2c_address, reg_pwr, 2) #read pwr to clear CVRF
                if val[1] & 0b00000010 == 0b00000010:
                    val = int(format(val[0], '08b')+format(val[1], '08b')[0:5], 2)
                    v = float(val) * lsb
                    print(v)
                    stat_logger.write_stat(v, 'v_pv')
                    break
            #read NO
            p6.on()
            time.sleep(1)
            while True:
                val = bus.read_i2c_block_data(i2c_address, reg_busv, 2) #check CVRF
                pwr = bus.read_i2c_block_data(i2c_address, reg_pwr, 2) #read pwr to clear CVRF
                if val[1] & 0b00000010 == 0b00000010:
                    val = int(format(val[0], '08b')+format(val[1], '08b')[0:5], 2)
                    v = float(val) * lsb
                    print(v)
                    stat_logger.write_stat(v, 'i_pv')
                    break
        except:
            unixTime = time.time()
            print(str(unixTime)+" error! just try again.")

read_busv()

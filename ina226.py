import smbus, subprocess, stat_logger, time
from gpiozero import InputDevice, OutputDevice

#relay is ACTIVE LOW
p5 = OutputDevice(5, active_high=False)
p6 = OutputDevice(6, active_high=False)
####

i2c_ch = 1

i2c_address = 0x40

reg_config = 0x00
reg_busv = 0x02
reg_mask_enable = 0x06

lsb = float(1.25/1000)

bus = smbus.SMBus(i2c_ch)

#set reg_config
val = bus.read_i2c_block_data(i2c_address, reg_config, 2)
val[0] = 0b01001111
val[1] = 0b11100110
bus.write_i2c_block_data(i2c_address, reg_config, val)

def read_busv():
        while True:
                try:
                        #read NC
                        p5.off()
                        while True:
                                val = bus.read_i2c_block_data(i2c_address, reg_mask_enable, 2) #read reg to clear flag
                                if val[1] == 0b1000:
                                        #read voltage measured
                                        val = bus.read_i2c_block_data(i2c_address, reg_busv, 2)
                                        val = int(format(val[0], '08b')+format(val[1], '08b'), 2)
                                        v = float(val) * lsb
                                        print(v)
                                        stat_logger.write_stat(v, 'v_bat')
                                        break
                        #read NO
                        p5.on()
                        while True:
                                val = bus.read_i2c_block_data(i2c_address, reg_mask_enable, 2) #read reg to clear flag
                                if val[1] == 0b1000:
                                        #read voltage measured
                                        val = bus.read_i2c_block_data(i2c_address, reg_busv, 2)
                                        val = int(format(val[0], '08b')+format(val[1], '08b'), 2)
                                        v = float(val) * lsb
                                        print(v)
                                        stat_logger.write_stat(v, 'i_load')
                                        break

                except:
                        unixTime = time.time()
                        print(str(unixTime)+" error! just try again.")

read_busv()

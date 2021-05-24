#miners addr
#192.168.1.158 = vega56 = 2C:F0:5D:5A:34:AC
#192.168.1.152 = gtx970 = E0:3F:49:A4:0C:00
import time, miner_ctrl, logging, stat_logger

logging.basicConfig(filename='stats/log', level=logging.DEBUG, format="%(asctime)s | %(message)s", datefmt="%d-%m-%Y %H:%M:%S")

lat = float(0)

miner_stat = miner_ctrl.message('192.168.1.158', 'ping')


while True:
	try:
		v_pv = float(stat_logger.read_stat('v_pv'))
		i_pv = float(stat_logger.read_stat('i_pv'))
		v_bat = float(stat_logger.read_stat('v_bat'))
		i_load = float(stat_logger.read_stat('i_load'))
		p_pv = v_pv*i_pv
		p_out = v_bat*i_load

		logging.debug(format(v_pv, '.2f')+" | "+format(i_pv, '.2f')+" | "+format(p_pv, '.2f')+" | "+format(v_bat, '.2f')+" | "+format(i_load, '.2f')+" | "+format(p_out, '.2f'))

		if miner_stat == "pong" and v_bat < 24.1:
			print("sleep")
			miner_ctrl.message("192.168.1.158", "sleep")
			miner_stat = None
		elif v_bat > 27:
			miner_ctrl.wake("2C:F0:5D:5A:34:AC")
			miner_stat = "pong"

		time.sleep(60)
	except:
		unixTime = time.time()
        print(str(unixTime)+" error! just try again.")

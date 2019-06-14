from subprocess import PIPE, Popen

def get_cpu_temperature():
    """get cpu temperature using vcgencmd"""
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])


while True:
	with open("cpu.log","w+") as f:
		temp = get_cpu_temperature()
		f.write(temp + "\r\n")
		time.sleep(1)

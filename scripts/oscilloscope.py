import serial
import serial.serialutil
import threading
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.ion()
threadLock = threading.Lock()
result = []


def read_data():
    global result
    connection = serial.Serial()
    try:
        connection = serial.Serial(port='/dev/ttyACM0', baudrate=230400)
        while connection.isOpen():
            if connection.inWaiting() > 0:
                data = connection.readline()
                if result != '':
                    threadLock.acquire()
                    result.append(data)
                    threadLock.release()
    except serial.SerialException, err:
        print 'Error occured while opening device %s' % err
    finally:
        connection.close()


def draw_plot():
    global result
    NUM_SAMPLES = 500
    while True:
        try:
            if len(result) > NUM_SAMPLES:
                samples = result[0:NUM_SAMPLES]
                value = []
                time = []
                threadLock.acquire()
                result = result[NUM_SAMPLES:]
                threadLock.release()
                for sample in samples:
                    temp = sample.split(',')
                    if len(temp) == 2:
                        value.append(int(temp[0].strip()))
                        time.append(int(temp[1].strip())/1000000.0)
                time_axis = []
                for index in xrange(len(time)):
                    time_axis.append(time[index] - time[0])
                ax.clear()
                ax.set_xlim(0, time_axis[-1])
                ax.set_ylim(-1000, 5000)
                ax.set_xlabel('time (us)')
                ax.set_ylabel('Voltage')
                ax.plot(time_axis, value)
                plt.pause(0.05)
        except KeyboardInterrupt:
            break
        except Exception:
            pass
        #print 'result length: ' + str(len(result))


def main():
    try:
        read_thread = threading.Thread(target=read_data, args=())
        read_thread.start()
        draw_plot()
    except Exception, e:
        print 'Error: Unable to start threads %s' % e

if __name__ == '__main__':
    main()

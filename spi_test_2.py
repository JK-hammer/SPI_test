# for 48LM01
import spidev
import time

spi = spidev.SpiDev()

spi.open(0, 1)
# open Port on SPI0, CE1 (Pins: 19-MOSI, 21-MISO, 23-CLK, 26-CE1)

spi.mode = 0
spi.bits_per_word = 8
spi.max_speed_hz = 500000  # value in Hz; Min value is 500kHz


# Write Function

def write_data(start_add, writedata):
    msg = [0x02]
    msg.extend(start_add)
    msg.extend(writedata)
    # print (msg) #for debugging
    spi.writebytes([0x06])
    time.sleep(0.01)
    spi.xfer(msg)


# End of Wrire Function


# Read Function

def read_data(start_add, byte_to_read):
    msg2 = [0x03]
    msg2.extend(start_add)

    for i in range(byte_to_read):
        msg2.append(0x00)

    # print (msg2) #for debugging
    rcv = spi.xfer(msg2)

    read_out = []
    for i in range(byte_to_read):
        read_out.append(rcv[4 + i])
    print('read data:', read_out)


# End of Read Function


# Main

add = [0x00, 0x00, 0x3a]
wdata = [0x0a, 0x0b, 0x0c]
nbyte = 3

write_data(add, wdata)  # call write function
time.sleep(0.5)
read_data(add, nbyte)  # call read function

time.sleep(0.1)

spi.close()  # close SPI Port

# end of Main

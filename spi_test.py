# SPI test with 48LM01 SPI EERAM
import spidev
import time

spi = spidev.SpiDev()

spi.open(0, 1)
# open port SPI0, using chip enable CE1 pin (Pins: 19-MOSI, 21-MISO, 23-CLK, 26-CE1)


# spi.mode = 0
spi.bits_per_word = 8
spi.max_speed_hz = 500000  # 500kHz

# write ops
spi.writebytes([0x06])
# 0x06 --> Write enable


msg = [0x02, 0x00, 0x00, 0x1a, 0x0a, 0x0b, 0x09, 0x0d, 0x0e]
# 0x02 --> write opertion
# 0x00, 0x00, 0x1a --> 3 bytes address
# 0x0a, 0x0b, 0x09, 0x0d, 0x0e --> 5 bytes of data


# transfer data
spi.xfer(msg)

# delay
time.sleep(0.5)

# Read ops - read multiple bytes from starting address
msg2 = [0x03, 0x00, 0x00, 0x1a, 0x00, 0x00, 0x00, 0x00, 0x00]
# 0x03 --> read operation
# 0x00, 0x00, 0x1a --> 3 bytes address
# 0x00, 0x00, 0x00, 0x00, 0x00 --> place holder to read 5 bytes


# Read ops - read single byte at the starting address
# msg2 = [0x03, 0x00, 0x00, 0x1e, 0x00]

# transfer data and read data; save read data to the list called 'rcv'
rcv = spi.xfer(msg2)

# print out 'rcv' to check
print(rcv)

# close SPI port
spi.close()

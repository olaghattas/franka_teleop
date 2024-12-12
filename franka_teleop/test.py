import hid
import time
# for d in hid.enumerate():
#     keys = list(d.keys())
#     keys.sort()
#     for key in keys:
#         print("%s : %s" % (key, d[key]))
#     print()

def convert(b1, b2):
    """Converts two 8-bit bytes to a signed 16-bit integer."""
    x = (b1) | (b2 << 8)
    if x >= 32768:
        x = -(65536 - x)
    return x

h = hid.device()
print("Opening the device")
h.open(9583, 50734)
while True:
    d = h.read(13)
    if d is not None:
        print(f"Data received: {d}")
        if d[0] == 1:
            print(f"6-DoF Data: x={convert(d[3], d[4])}, y={convert(d[1], d[2])}, z={convert(d[5], d[6])}, roll={convert(d[7], d[8])}, pitch={convert(d[9], d[10])}, yaw={convert(d[11], d[12])}")
        elif d[0] == 3:
            print(f"Button Data: {d[1]}")
    else:
        print("No data received")
    time.sleep(0.1)
import imu
import machine as mn
import utime as ut

i2c = mn.I2C(1, sda=mn.Pin(6), scl=mn.Pin(7), freq=400000)
mpu = imu.MPU6050(i2c)

while True:
    # print("x:", mpu.accel.x, "y:", mpu.accel.y, "z:", mpu.accel.z)
    print("A:", mpu.gyro.x, "B:", mpu.gyro.y, "Y:", mpu.gyro.z)
    ut.sleep(1)
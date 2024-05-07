class SBUSConsts:
    BAUD_RATE = 98000
    NUM_CHANNELS = 16
    SBUS_HEADER = b'\x0F'
    SBUS_FOOTER = b'\x00'
    SBUS_TIMEOUT_MS = 7
    PAYLOAD_SIZE = 25
    SBUS_LOST_FRAME = b'\x04'
    SBUS_FAILSAFE = b'\x08'
    DEFAULT_MIN = 172
    DEFAULT_MAX = 1811

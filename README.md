# uMessageRouter
Route messages between threads in MicroPython.

Will likely use the _thread library in the loboris MicroPython port: https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/thread.

Current concept:
 - Threads started
 - Thread 1 subscribes to topic info
 - Router adds an list to the subscription dictionary called info and adds thread 1 ID
 - Thread 2 sends message to topic info
 - Router sends message to all threads in the info topic thread list

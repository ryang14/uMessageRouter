# uMessageRouter
Route messages between tasks in MicroPython.

Will likely use the _thread library in the loboris MicroPython port: https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/thread.

Initial concept:
 - Router/main task started
 - Worker tasks started
 - Worker 1 task subscribes to topic info
 - Router adds an list to the subscription dictionary called info and adds worker 1 queue
 - Worker 2 sends { info: data } to router queue
 - Router sends { info: data } to all queues in the info topic queue list

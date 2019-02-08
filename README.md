# uMessageRouter
Route messages between tasks in MicroPython.

Will likely use the _thread library in the loboris MicroPython port: https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/thread.

Current concept:
 - Worker tasks started
 - Worker 1 task subscribes to topic info
 - Router adds an list to the subscription dictionary called info and adds worker 1 task
 - Worker 2 sends message to topic info
 - Router sends message to all tasks in the info topic task list

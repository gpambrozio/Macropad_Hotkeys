local obj={}
obj.__index = obj

-- Metadata
obj.name = "Macropad"
obj.version = "0.1"
obj.author = "Gustavo Ambrozio <gustavo@gustavo.eng.br>"
obj.homepage = "https://github.com/gpambrozio/Macropad_Hotkeys/tree/master/Macropad.spoon"
obj.license = "MIT - https://opensource.org/licenses/MIT"

obj.serial = nil

function executeMenu(descriptor)
    local application, parameters = descriptor:match("^([^,]+),(.+)")
    if application == nil or parameters == nil then
        return
    end
    local app = hs.appfinder.appFromName(application)
    local items = {}
    for str in parameters:gmatch("([^,]+)") do
        table.insert(items, str)
    end

    local menuItem = app:findMenuItem(items)
    if menuItem ~= nil then
        app:selectMenuItem(items)
    else
        print("Can't find " ..  hs.inspect(items))
    end
end

function serialWatcher(serialPortObject, callbackType, message, hexadecimalString)
    if callbackType == "received" then
        print("message: " .. message)
        local command, parameters = message:match("^(%a+): (.+)\n")
        if command ~= nil then
            if command == "menuItem" then
                executeMenu(parameters)
            end
        end
    end
end

function sendToSerial(message)
    print("sending to serial:  " .. message)
    if obj.serial == nil then
        print("not connected")
        return
    end
    obj.serial:sendData(message .. "\n")
end

function connectToUSB()
    if obj.serial ~= nil and obj.serial:isOpen() then
        print("already connected")
        return
    end

    local devices = hs.usb.attachedDevices()
    local found = false
    for i, device in pairs(devices) do
        if device["productName"] == "Macropad RP2040" then
            found = true
            break
        end
    end

    if not found then
        print("didn't find device")
        return
    end

    local portNames = hs.serial.availablePortNames()
    table.sort(portNames)
    local port = portNames[#portNames]
    local path = "/dev/cu." .. port
    print("will try to connect to " .. path)

    obj.serial = hs.serial.newFromPath(path)
    obj.serial:baudRate(115200)
    obj.serial:callback(serialWatcher)
    obj.serial:open()
end

obj.diskWatcher = hs.pathwatcher.new("/Volumes", function(paths, flagTables)
    for k, v in pairs(paths) do
        if v == "/Volumes/CIRCUITPY" and flagTables[k]["itemCreated"] == true then
            connectToUSB()
            return
        end
    end
end)
obj.diskWatcher:start()

function applicationWatcher(appName, eventType, appObject)
    if appName ~= nil and eventType == hs.application.watcher.activated then
        sendToSerial("appChanged: " .. appName)
    end
end
obj.appWatcher = hs.application.watcher.new(applicationWatcher)
obj.appWatcher:start()

function sleepEvent(event)
    events = {
        [hs.caffeinate.watcher.screensDidWake] = false,
        [hs.caffeinate.watcher.screensDidUnlock] = false,
        [hs.caffeinate.watcher.systemDidWake] = false,
        [hs.caffeinate.watcher.screensaverDidStop] = false,
        [hs.caffeinate.watcher.sessionDidBecomeActive] = false,
        [hs.caffeinate.watcher.screensaverDidStart] = true,
        [hs.caffeinate.watcher.screensDidLock] = true,
        [hs.caffeinate.watcher.screensDidSleep] = true,
        [hs.caffeinate.watcher.sessionDidResignActive] = true,
        [hs.caffeinate.watcher.systemWillSleep] = true,
        [hs.caffeinate.watcher.systemWillPowerOff] = true
    }
    sleep_on_off = events[event]
    if sleep_on_off ~= nil then
        sendToSerial("sleep: " .. (sleep_on_off and "on" or "off"))
    end
end
obj.sleepWatcher = hs.caffeinate.watcher.new(sleepEvent)
obj.sleepWatcher:start()

connectToUSB()

return obj

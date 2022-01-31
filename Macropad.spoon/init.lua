local obj={}
obj.__index = obj

-- Metadata
obj.name = "Macropad"
obj.version = "0.1"
obj.author = "Gustavo Ambrozio <gustavo@gustavo.eng.br>"
obj.homepage = "https://github.com/Hammerspoon/Spoons"
obj.license = "MIT - https://opensource.org/licenses/MIT"

local serial = nil

-- From https://stackoverflow.com/a/27028488
function dump(o)
    if type(o) == 'table' then
        local s = '{ '
        for k,v in pairs(o) do
            if type(k) ~= 'number' then k = '"'..k..'"' end
            s = s .. '['..k..'] = ' .. dump(v) .. ','
        end
        return s .. '} '
    else
        return tostring(o)
    end
end

function executeMenu(descriptor)
    local application, parameters = string.match(descriptor, "^([^,]+),(.+)")
    if application == nil or parameters == nil then
        return
    end
    local app = hs.appfinder.appFromName(application)
    local items = {}
    for str in string.gmatch(parameters, "([^,]+)") do
        table.insert(items, str)
    end

    local menuItem = app:findMenuItem(items)
    if menuItem ~= nil then
        app:selectMenuItem(items)
    else
        print("Can't find " ..  dump(items))
    end
end

function serialWatcher(serialPortObject, callbackType, message, hexadecimalString)
    if callbackType == "received" then
        print("message: " .. message)
        local command, parameters = string.match(message, "^(%a+): (.+)\n")
        if command ~= nil then
            if command == "menuItem" then
                executeMenu(parameters)
            end
        end
    end
end

function sendToSerial(message)
    print("sending to serial:  " .. message)
    if serial == nil then
        print("not connected")
        return
    end
    serial:sendData(message .. "\n")
end

function connectToUSB()
    if serial ~= nil and serial:isOpen() then
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
        return
    end

    local portNames = hs.serial.availablePortNames()
    table.sort(portNames)
    local port = portNames[#portNames]
    local path = "/dev/cu." .. port

    serial = hs.serial.newFromPath(path)
    serial:baudRate(115200)
    serial:callback(serialWatcher)
    serial:open()
end

hs.serial.deviceCallback(function(devices)
    connectToUSB()
end)

function applicationWatcher(appName, eventType, appObject)
    if (eventType == hs.application.watcher.activated) then
        sendToSerial("appChanged: " .. appName)
    end
end
appWatcher = hs.application.watcher.new(applicationWatcher)
appWatcher:start()

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
sleepWatcher = hs.caffeinate.watcher.new(sleepEvent)
sleepWatcher:start()

connectToUSB()

return obj
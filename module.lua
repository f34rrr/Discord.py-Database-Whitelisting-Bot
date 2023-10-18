--[[

add this in your mm or smth

]]

local plr = game.Players.LocalPlayer
local url = "https://database-wl.<YOUR REPLIT USER>.repl.co/api/wl/"
local HttpService = game:GetService("HttpService")
local data = HttpService:JSONDecode(HttpService:GetAsync(url .. plr.Name))

if data["wl"] == "yes" then
    game:GetService("StarterGui"):SetCore("SendNotification",{
        Title = "sucess",
        Text = "yes!!"
    })
elseif data["wl"] == "no" then
    game:GetService("StarterGui"):SetCore("SendNotification",{
        Title = "error",
        Text = "oughh no!"
    })
end
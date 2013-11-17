require 'sqlite3'
require 'socket'

server = TCPServer.open(80)
loop{
    Thread.start(server.accept) do |client|
        
    end
}


db = SQLite3::Database.new("data.db")
db.execute("UPDATE data SET hits = 0")
#=begin
db.execute("UPDATE data SET hits = hits + 1 WHERE time = ?", "9:00")
db.execute("UPDATE data SET hits = hits + 1 WHERE month = ?", "11")
db.execute("UPDATE data SET hits = hits + 1 WHERE day = ?", "09")
db.execute("UPDATE data SET hits = hits + 1 WHERE radiation = ?", 120)
db.execute("UPDATE data SET hits = hits + 1 WHERE humidity = ?", 0.6)
db.execute("UPDATE data SET hits = hits + 1 WHERE temp = ?", 2)
db.execute("UPDATE data SET hits = hits + 1 WHERE wind = ?", 6)
#=end
i = 0
temp = 0
db.execute("SELECT id FROM data WHERE hits >= 5") do |row|
    i = i + 1
    #puts(row)
    temp = temp + row[0]
end
puts(temp/i)
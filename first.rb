=begin
This is my Ruby program as a 
refresher course
=end

puts "First Ruby program"

class Sample
    @@out = "Pranav"
    def say
        puts "#@@out"
        hsh = {"batman" => 12, "superman" => 150, "flash" => 600}
        hsh.each do | key, value|
            print key, " : ", value, "\n"
        end
    end

    def iterate(num=10)
        print num
        for i in 0..5
            print "\n", i, "\n"        
        end
    end
end

obj = Sample.new
obj.say()
obj.iterate(100)
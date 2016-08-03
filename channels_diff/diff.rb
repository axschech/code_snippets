arrs = [[],[]]
current = 0

File.read('channels.txt').each_line do |line|
    if line === "\n" && current === 0
        current = 1
        next
    end
    arrs[current].push(line.chomp)
end

puts arrs[0] - arrs[1]

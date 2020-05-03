i = 0
puts 'while'
#while#
while i < 10
  puts i
  i += 1
end
puts 'until'
#until#
until i == 0
  puts i
  i -= 1
end
puts 'loops and break'
#loops + break#
loop do
  i += 1
  puts i
  break if i == 10
end
puts 'loops and next'
#loop + next#
loop do
  i -= 1
  next if i > 0 #continue#
  puts i
  break if i == -2
end
